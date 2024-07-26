import requests,os,re,time,threading
from multiprocessing import Pool, cpu_count
from bs4 import BeautifulSoup as bs

# 图片存放路径
# SAVE_PATH = "d:\MyCloud\MyAliCloud\Workspace\Python\myPy3L\download"
SAVE_PATH = "download"
CRAWLER_URL = "https://desk.zol.com.cn{}"
"""
    可选的图片尺寸
    4096x2160(4k)
    2560x1440(2k)
    1920x1200
    1920x1080   默认，15-23英寸
"""
CURRENT_PIX = "1920x1080"

"""
X-Requested-With请求头用于在服务器端判断request来自Ajax请求还是传统请求：
    如果 requestedWith 为 null，则为同步请求，返回普通html文本；
    如果 requestedWith 为 XMLHttpRequest 则为 Ajax 异步请求，返回json数据。
"""
HEADERS = {
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}

HEADERS2 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0", }

def mkdir(folder_name):
    """
    新建文件夹，并切换到该目录下
    :param folder_name: 文件夹名称
    :return: True为创建成功，False为创建失败
    """
    path = os.path.join(SAVE_PATH, folder_name)
    if not os.path.exists(path):
        # 创建文件夹
        os.makedirs(path)
        print("Create a folder ", path)
        # 要切换到新的path路径
        os.chdir(path)
        return True
    print("Folder has existed!")
    return False

def save_images(img_src, img_name):
    """
    保存图片
    :param img_src: 图片地址
    :param img_name: 图片名称
    :return: None
    """
    try:
        img = requests.get(img_src, headers=HEADERS2)
        expected_length = int(img.headers.get("Content-Length", 0))
        if expected_length is not None:
            actual_length = img.raw.tell()
            expected_length = int(expected_length)
            if actual_length < expected_length:
                raise IOError(
                    'incomplete read ({} bytes read, {} more expected)'.format(
                        actual_length,
                        expected_length - actual_length
                    )
                )
        
        with open(SAVE_PATH + "\\" + img_name + ".jpg", "ab") as file:
            file.write(img.content)
            print("{}.jpg save successfully!".format(img_name))
    except:
        pass

def clear(dir_path):
    """
    删除空文件夹
    :param dir_path: 文件夹路径
    :return None
    """
    if os.path.exists(dir_path):
        if os.path.isdir(dir_path):
            for file in os.listdir(dir_path):
                c_path = os.path.join(dir_path, file)
                if os.path.isdir(c_path):
                    # 递归删除空文件夹
                    clear(c_path)
        if not os.listdir(dir_path):
            os.rmdir(dir_path)
            print("Remove the empty folder:{}".format(dir_path))

def get_urls():
    """
    获取壁纸套图地址
    https://desk.zol.com.cn
    https://desk.zol.com.cn/4096x2160/
    https://desk.zol.com.cn/2560x1440/

    """
    url = "https://desk.zol.com.cn/pc/{}.html"

    # 创建一个无序不重复元素集
    _urls = set()
    # 获得前3页图片地址
    for url in [url.format(page) for page in range(1, 3)]:
        html = requests.get(url, headers=HEADERS).text
        
        """
            re模块为 正则表达式模块
            re.findall函数：在字符串中找到正则表达式所匹配的所有子串，
                如果找到匹配的，则返回一个列表，
                如果没有找到匹配的，则返回空列表。
            注意： match 和 search 函数是匹配一次，findall函数匹配所有。
        """
        for u in [
            CRAWLER_URL.format(u)
            for u in re.findall('<a class="pic" href="(.*?)"', html)
        ]:
            # 去掉软件下载的内容
            _exe = re.findall('.exe',u)
            if _exe:
                continue
            else:
                _urls.add(u)
                # print(u)
        
    return _urls

lock = threading.Lock()

def getPhotoListBox(html):
    soup = bs(html, 'html.parser')
    fragment = soup.find('div',class_='photo-list-box').find_all('li')
    
    return fragment

def run(url):
    """
    启动爬虫
    """
    html = requests.get(url, headers=HEADERS).text
    # print("html = ",html)
    
    # 壁纸套图名，也作文件夹名；使用re的非贪婪方式获取
    title = re.findall('<a id="titleName" href=.*?>(.*?)</a>', html)[0]
    print("title = ",title)
    # 壁纸套图张数
    max_cnt = re.findall(
        '<span>（<span class="current-num">(.*?)）</span>', html)[0].split("/")[-1]
    print("max_cnt = ",max_cnt)
    cnt = 0
    with lock:
        if not mkdir(title):
            return
        for _ in range(int(max_cnt)-1):
            img_url = re.findall('<a target="_blank" id="'+CURRENT_PIX+'" href="(.*?)">'+CURRENT_PIX+'</a>', html)
            # print("img_url = ",img_url)
            print("current cnt = ",cnt)
            fragment = getPhotoListBox(html)
            cnt = cnt + 1
            print("next cnt = ",cnt)
            # print("fragment[next cnt] = ",str(fragment[cnt]))
            
            next_page = re.findall('<a href="(.*?)">', str(fragment[cnt]))
            # print("next_page = ",next_page)
            
            img = img_url[0] if img_url else []
            if img:
                req = requests.get(CRAWLER_URL.format(img), headers=HEADERS).text
                print("img_full_url = ",CRAWLER_URL.format(img))
                # print("req = ",req)
                img_src = re.findall('<img src="(.*?)"', req)[0]
                print("img_src = ",img_src)
                save_images(img_src, img[-12:-5])
                html = requests.get(CRAWLER_URL.format(next_page[0]), headers=HEADERS).text
            

if __name__ == "__main__":
    urls = get_urls()
    # print("urls = ",urls)
    cpu_cnt = cpu_count()
    print("processess count = ",cpu_cnt)
    """
    用这个方法会造成文件夹下生成文件夹的情况。不建议使用。
    for url in urls:
        run(url)
    """

    # 进程池：定义当前cpu数量的进程池对象
    pool = Pool(processes=cpu_count())

    try:
        pool.map(run, urls)
    except:
        time.sleep(30)
        pool.map(run, urls)
    pool.close()
    
    # 去除像素大小不符合要求的文件夹
    clear(SAVE_PATH)
    
