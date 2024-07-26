# 导入urllib库
from urllib import request,error
import socket

# timeout参数,可以设置超时时间，单位为秒，意思就是如果请求超出了设置的这个时间还没有得到响应，就会抛出异常，如果不指定，就会使用全局默认时间。它支持 HTTP 、 HTTPS 、 FTP 请求。
# 注意，这里timeout=1秒，会报urllib.error.URLError异常，错误原因是 timed out 。
# 因此我们可以通过设置这个超时时间来控制一个网页如果长时间未响应就跳过它的抓取，利用 try,except 语句就可以实现这样的操作。
print("测试urlopen函数，timeout参数")
try:
    response = request.urlopen("http://httpbin.org/get",timeout=0.1)
except error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print("TIME OUT!")
    else:
        print(e.read())