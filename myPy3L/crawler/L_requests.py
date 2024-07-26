import requests as rq
"""
Requests库有两个重要对象，分别是Request和Response。
    Request对象对应的是请求，向目标网址发送一个请求访问服务。
    Response对象，是包含了爬虫返回的内容。

rq.get(url, params, args)   发送 GET 请求到指定 url
rq.delete(url, args)        发送 DELETE 请求到指定 url
rq.head(url, args)          发送 HEAD 请求到指定 url
rq.patch(url,data,args)     发送 PATCH 请求到指定 url
rq.post(url,data,json,args) 发送 POST 请求到指定 url
rq.put(url,data,args)       发送 PUT 请求到指定 url
rq.request(method,url,args) 向指定的 url 发送指定的请求方法

"""
url = "https://sj.zol.com.cn/bizhi/1080x1920/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}
"""
[1] requests.get(url,params=None,**kwargs) 
获取网页
    url: 想要获取的网页的链接。
    params: url的额外参数，字典或字节流格式，可选。
    **kwargs: 12个控制访问的参数。
"""
response = rq.get(url.format(), headers=headers)

print(response.status_code)  # 返回 http 的状态码，比如 404 和 200（200 是 OK，404 是 Not Found）
print(response.headers)  # 返回响应头，字典格式
print(response.content)  # 返回响应的内容，以字节为单位
print (response.encoding)   # 查看响应头部字符编码，解码 r.text 的编码方式
print(response.reason)  # 响应状态的描述，比如 "Not Found" 或 "OK"
print(response.request)  # 返回请求此响应的请求对象
print(response.apparent_encoding)  # 返回编码
print (response.url)    # 返回响应的 URL完整地址
print(response.text)    # 返回响应的内容，返回的是Unicode格式的数据
print(response.cookies)  # 返回一个 CookieJar 对象，包含了从服务器发回的 cookie
print (response.links)    # 返回响应的解析头链接
# print(response.json())  # 返回 json 数据
# print(response.close())    # 关闭与服务器的连接

"""
[2] requests.post(url, data={key: value}, json={key: value}, args)
post() 方法可以发送 POST 请求到指定 url
    url 请求 url。
    data 参数为要发送到指定 url 的字典、元组列表、字节或文件对象。
    json 参数为要发送到指定 url 的 JSON 对象。
    args 为其他参数，比如 cookies、headers、verify等。
"""
# 表单参数，参数名为 fname 和 lname
mydata = {'fname': 'RUNOOB','lname': 'Boy'}

url_post = rq.post('https://www.runoob.com/try/ajax/demo_post2.php', data = mydata, headers=headers)
print("print url_post = ", url_post.text)
