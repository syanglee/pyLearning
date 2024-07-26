from urllib import request, parse

"""
[1] urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
用于打开一个URL地址，并返回一个文件对象。
参数：
    url (string)：要打开的URL地址。
    data (可选)：data 参数是可选的，如果要添加 data ，它要是字节流编码格式的内容，即 bytes 类型，通过 bytes() 函数可以进行转化；
                另外如果你传递了这个 data 参数，它的请求方式就不再是 GET 方式请求，而是 POST 。
    timeout (可选)：超时时间，单位为秒。
返回值：
    file：返回一个文件对象，可以读取文件内容。
"""
response = request.urlopen('https://www.baidu.com')
page = response.read()
html_content = page.decode('utf-8')
print("查看页面内容：\n",html_content)

response = request.urlopen('https://python.org/')
print("查看 response 的返回类型：",type(response))
print("查看反应地址信息: ",response)
print("查看头部信息1 (http header)：\n",response.info())
print("查看头部信息2 (http header)：\n",response.getheaders())
print("输出头部属性信息：",response.getheader("Server"))
print("查看响应状态信息1(http status)：",response.status)
print("查看响应状态信息2(http status)：",response.getcode())
print("查看响应 url 地址：",response.geturl())


# data类型是bytes的，这里传递的参数是word，值是hello；
# 用parse.urlencode() 方法来将参数字典转化为字符串，并使用utf8编码格式
data = bytes(parse.urlencode({'word': 'hello'}), encoding='utf8')
response2 = request.urlopen('http://httpbin.org/post', data=data)
print(response2.read().decode("utf-8"))
"""
[2] urllib.request.urlretrieve()
用于下载一个URL地址的数据，并将其保存到本地。
参数：
    url (string)：要下载的URL地址。
    filename (string)：要保存的文件名。
    reporthook (可选)：用于报告下载进度。
    data (可选)：要发送的数据，仅在使用POST方法时使用。
    timeout (可选)：超时时间，单位为秒。
返回值：
    None

"""
request.urlretrieve('https://www.example.com', 'download/example.txt')

"""
[3] urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
参数：
    url：是请求链接，这个是必传参数，其他的都是可选参数。
    data：如果要传必须传 bytes （字节流）类型的，如果是一个字典，可以先用 urllib.parse.urlencode() 编码。
    headers：是一个字典，你可以在构造 Request 时通过 headers 参数传递，也可以通过调用 Request 对象的 add_header() 方法来添加请求头。请求头最常用的用法就是通过修改 User-Agent 来伪装浏览器，默认的 User-
    Agent：Python-urllib ，你可以通过修改它来伪装浏览器，比如要伪装火狐浏览器，你可以把它设置为 Mozilla/5.0 (X11; U; Linux i686)Gecko/20071127 Firefox/2.0.0.11
    origin_req_host：指的是请求方的 host 名称或者 IP 地址。
    unverifiable：指的是这个请求是否是无法验证的，默认是 False 。意思就是说用户没有足够权限来选择接收这个请求的结果。例如我们请求一个HTML文档中的图片，但是我们没有自动抓取图像的权限，这时 unverifiable 的值就是 True 。
    method：是一个字符串，它用来指示请求使用的方法，比如 GET ， POST ， PUT 等等。
返回值：

"""
url = "http://httpbin.org/post"
headers = {
    #伪装一个火狐浏览器
    "User-Agent":'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    "host":'httpbin.org'
}
dict = {
    "name":"Germey"
}
data2 = bytes(parse.urlencode(dict),encoding="utf8")
req = request.Request(url=url, data=data2, headers=headers, method="POST")
resp = request.urlopen(req)
print(resp.read().decode("utf-8"))

# headers 也可以用 add_header() 方法来添加。
req = request.Request(url=url, data=data, method='POST')
req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5;Windows NT)')

"""
urllib.request高级特性
urllib.request.BaseHandler ，它是所有其他 Handler 的父类，它提供了最基本的 Handler 的方法，例
如 default_open() 、 protocol_request() 等。
下面是继承BaseHandler的各种子类：
    HTTPDefaultErrorHandler: 用于处理HTTP响应错误，错误都会抛出 HTTPError 类型的异常。
    HTTPRedirectHandler: 用于处理重定向。
    HTTPCookieProcessor: 用于处理 Cookie 。
    ProxyHandler: 用于设置代理，默认代理为空。
    HTTPPasswordMgr: 用于管理密码，它维护了用户名密码的表。
    HTTPBasicAuthHandler: 用于管理认证，如果一个链接打开时需要认证，那么可以用它来解决认证问题。 
其他的 Handler ，可以参考官方文档（https://docs.python.org/3/library/urllib.request.html#urllib.request.BaseHandler）
"""

"""
urllib.request.OpenerDirector ，
urllib.request.urlopen() 这个方法实际上就是一个 Opener 。

"""
auth_handler = request.HTTPBasicAuthHandler()
auth_handler.add_password(  realm='PDQ Application',
                            uri='https://mahler:8092/site-updates.py',
                            user='klem',
                            passwd='kadidd!ehopper')
opener = request.build_opener(auth_handler)
request.install_opener(opener)
request.urlopen('http://www.example.com/login.html')


# 添加代理
proxy_handler = request.ProxyHandler({
'http': 'http://218.202.111.10:80',
'https': 'https://180.250.163.34:8888'
})
opener = request.build_opener(proxy_handler)
response = opener.open('https://www.baidu.com')
print(response.read())