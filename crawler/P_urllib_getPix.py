from urllib import request
from bs4 import BeautifulSoup as bs
from PIL import Image

# 定义一个url
# url = "https://www.vilipix.com/p/fd82ad939e4348c78ece772b9176f780"
url = "https://www.vilipix.com/illust/110823043"

# data = bytes(urllib.parse.urlencode({"name":"frok"}),encoding="utf-8")

#伪装成一个火狐浏览器
# headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'}
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
headers = {"Referer": "Referer: http://desk.zol.com.cn/dongman/1920x1080/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36", }

# 使用urllib.request.urlopen()函数打开url
# req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
req = request.Request(url=url, headers=headers, method="POST")
resp = request.urlopen(req,timeout=15)

# 使用 BeautifulSoup 获得
soup = bs(resp.read().decode('utf-8'), 'html.parser')
# print(soup)

# 获取所有图片信息
all_imgs = soup.find_all('img')

# 初始化图片个数，从第一个开始计数
i = 1

# 获取当前待保持图片的路径 TODO: 考虑改写为Windows和Linux适配版本
# download_path = "d:\MyCloud\MyAliCloud\Workspace\Python\myPy3L\download"
download_path = "download"
print("download_path = ", download_path)

# 遍历所有图片信息，并将大小适合的图片下载到本地
for img in all_imgs:
    print("图片" + str(i) + "的脚本：")
    print(img)
    
    # 获取图片的源地址
    img_src = img['src']
    # print("输出图片的源地址：")
    # print(img_src)

    img_file = request.urlopen(img_src)
    img_ = Image.open(img_file)
    # 获得图片的尺寸；其返回值为tuple类型；
    img_size = img_.size
    # 获得图片的宽度
    w = img_.width
    # 获得图片的高度
    h = img_.height
    # 获得图片的格式
    f = img_.format
    print("图片" + str(i) + "的尺寸：" + str(w) + "x" + str(h) + " ；图片格式：" + str(f))

    # 计数
    i = i + 1

    # 只保存尺寸大于300x300图片
    if w > 300 and h > 300:
        # 获得页面中的实际图片名称
        img_name = img_src.split('?')[0].split('/')[-1]

        # 图片要保存路径，这里是WSL环境下当前开发环境的位置
        file_save_path = download_path + '/%s' % img_name
        
        # 保存图片到指定路径
        request.urlretrieve(img_src, file_save_path)
        print("成功保存图片：" + img_name)
        print("img_src = " + img_src)
        # request.urlretrieve("https://desk-fd.zol-img.com.cn/t_s1920x1080c5/g7/M00/0E/00/ChMkLGPHUaKIFKcmAAFutyYruMIAAL3OQAiwcEAAW7P023.jpg",file_save_path)
