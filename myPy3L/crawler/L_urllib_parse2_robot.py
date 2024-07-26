from urllib import request,parse,error,robotparser

# [6] urllib.robotparse
# 网站文件 robots.txt
# 每个网站都会定义 robots.txt 文件，这个文件可以告诉网络爬虫爬取该网站时存在哪些限制。作为良好网民以及其他人利益，一般上遵从这些限制。


rp = robotparser.RobotFileParser()
rp.set_url('https://www.douban.com/robots.txt')
rp.read()
url = 'https://www.douban.com'
user_agent = 'Wandoujia Spider'
wsp_info = rp.can_fetch(user_agent, url)
print("Wandoujia Spider 代理用户访问情况：",wsp_info)
user_agent = 'Other Spider'
osp_info = rp.can_fetch(user_agent, url)
print("Other Spider 代理用户访问情况：",osp_info)
