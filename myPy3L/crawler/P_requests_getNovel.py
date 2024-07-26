import requests
from bs4 import BeautifulSoup as bs


# http://www.wuxianxs.cc/read/11908/8761312.html

# 网页请求
def getHTMLText(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    try:
        reps = requests.get(url, headers=headers)

        reps.raise_for_status()
        
        reps.encoding = reps.apparent_encoding
        # print("网页访问成功: ",reps.text)
        return reps.text
    except:
        print("页面访问失败！",url)

# 获得章节列表
def getChapterList(url, html):
    home_url = url.split('/')[-2]
    # print("home_url",home_url)
    
    chapter_url_list = []

    soup = bs(html, "html.parser")
    a_list = soup.find("div",id="list").find_all('a')
    
    for a in a_list:
        if a.get("rel")==None:
            continue
        else:
            # print("a = ",a)
            a_url = "http://" + home_url + a.get("href")
            # print("a_url = ",a_url)

            name = a.get("title")            
            # print("name = ",name)

            chapter_url_list.append([a_url,name])
    return chapter_url_list

# 获得章节内容
def saveChapter(chapter_url_list):
    chapter_content = ""
    line_break = "\r\n"
    for url in chapter_url_list:
        html = getHTMLText(url[0])
        chapter_title = url[1].split('_')[0]
        book_name = ""
        soup = bs(html, "html.parser")
        a_list = soup.find("div",class_="con_top").find_all('a')
        for a in a_list:
            if a.get("href") == None:
                continue
            else:
                book_name = a.get("title")

        all_p = soup.find("div",id="booktxt").find_all('p')
        chapter_content = chapter_title + line_break
        for p in all_p:
            if p.text.endswith('，'):
                chapter_content = chapter_content + p.text
            else:
                chapter_content = chapter_content + p.text + line_break
        
        print("book_name = ",book_name)
        print("chapter_title = ",chapter_title)

        with open('download/{}.txt'.format(chapter_title), 'a') as f:
            f.write(chapter_content)
            print("当前下载章节：{}".format(chapter_title))
        
        return 1
    


# 主函数
def main():
    url = "http://www.wuxianxs.cc/txt11908.html"

    html = getHTMLText(url)

    chapter_url_list = getChapterList(url, html)

    saveChapter(chapter_url_list)

    
    pass

main()