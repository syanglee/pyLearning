import urllib.request

# 定义一个url
url = 'https://www.runoob.com/?s='

# 定义一个关键字
keyword = 'Python 教程'

# 将关键字转换为url编码
key_code = urllib.request.quote(keyword)

# 将url拼接，获得runoob网站中查询页面的url
url_all = url + key_code

# 定义一个头部信息
headers = {'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

# 创建一个请求对象
# req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
req = urllib.request.Request(url_all,headers=headers)

# 创建一个响应对象
reps = urllib.request.urlopen(req).read()

# 创建并打开一个文件
fh = open('./urllib_test_runoob_search.html','wb') 

# 将请求响应的内容写入打开的文件
fh.write(reps)

# 关闭文件
fh.close()