import requests,re
from lxml import etree
from fake_useragent import UserAgent

ZOL_URL = 'http://desk.zol.com.cn{}'

class wallpaper(object):
    def __init__(self):
        self.url = 'http://desk.zol.com.cn/1920x1080/hot_{}.html'
        # self.path = 'D:\MyCloud\MyAliCloud\Workspace\Python\myPy3L\download\\'    # Windows
        self.path = 'download/'  # Linux
        self.headers = {}
        ua = UserAgent()
        for i in range(1,10):
            self.headers = {
                'user-agent':ua.random
            }
    def get_html(self,url):
        html = requests.get(url,headers=self.headers)
        # 由于zol的页面中设置了text/html; charset=gb2312，因此内容需编码
        return html.content.decode('gb2312')
    def get_wallpaper(self,html):        
        target = etree.HTML(html)
        links=target.xpath('//li[@class="photo-list-padding"]/a/@href')
        print("links = ",links)
        return links
    def save_wallpaper(self,w_links):
        for link in w_links:
            _exe = re.findall('.exe',link)
            if _exe:
                continue
            else:
                img_url = ZOL_URL.format(link)
                print("img_url = ",img_url)
                html = requests.get(img_url,headers=self.headers).text
                t = etree.HTML(html)
                images = t.xpath('//div[@class="photo-list-box"]/ul/li/a/img/@src')
                # print("images = ",images)
                for image in images:
                    print("image = ",image)
                    htp = requests.get(image,headers=self.headers)
                    _file_name = image.split('/')[-1].split('.')[0]
                    with open('{}{}.jpg'.format(self.path,_file_name),'wb') as f:
                        f.write(htp.content)
            
    def main(self):
        #end_page = int(input("要爬多少页？"))
        end_page = 1
        for page in range(1,end_page+1):
            url = self.url.format(page)
            print("url = ",url)
            html = self.get_html(url)
            wallpaper_links = self.get_wallpaper(html)
            self.save_wallpaper(wallpaper_links)
            
if __name__ == '__main__':
    spider = wallpaper()
    spider.main()