from urllib import parse

# urllib.parse 分为 URL parsing (网址解析）和 URL quoting（地址引用） 。
# 1.urllib.parse
# [1] urllib.parse.urlparse(urlstring, scheme=”, allow_fragments=True)
url = r'https://docs.python.org/3/search.html?q=parse&check_keywords=yes&area=default'

# ParseResult(scheme='https', netloc='docs.python.org', path='/3/search.html', params='', query='q=parse&check_keywords=yes&area=default', fragment='')
urp = parse.urlparse(url)
print("urlparse 分解url地址:")
print(urp)
print("输出netloc：",urp.netloc)    

# 解析url中的最后的地址，一般为当前页面的文件名称；如果是图片的话，就是图片名称
print("解析url中的最后的地址:")
print(urp.path.split('/')[-1])

# [2] urllib.parse.urlunparse(parts)
# 从urlparse() 返回的元组元素构造一个URL 。该部分参数可以是任何六个组件的迭代。
print("【urlunparse】 将多个元组元素构造一个URL:")
parsed=parse.urlparse('http://user:pass@NetLoc:80/path;parameters?query=argument#fragment')
print(parsed)
url=parse.urlunparse(parsed)
print(url)

# [3] urllib.parse.parse_qs(qs, keep_blank_values=False, strict_parsing=False, encoding=’utf-8’, errors=’replace’)
query_param_dict = parse.parse_qs(urp.query)
print("【parse_qs】 返回字典：",query_param_dict)

#注意：加号会被解码，可能有时并不是我们想要的
pps = parse.parse_qs('proxy=183.222.102.178:8080&task=XXXXX|5-3+2')
print("【parse_qs】 分解url地址，返回字典:")
print(pps)

# [4] urllib.parse.parse_qsl(qs, keep_blank_values=False, strict_parsing=False, encoding=’utf-8’, errors=’replace’)
query_param_list = parse.parse_qsl(urp.query)
print("【parse_qsl】 返回列表：",query_param_list)

# [5] urllib.parse.urlsplit(urlstring, scheme=”, allow_fragments=True)
# 返回：(scheme, netloc, path, query, fragment) 比 urlparse() 少个params。该方法更常用。
# 五个参数分别是：寻址方案（addressing scheme），网络地址（network location），路径（path），查询（ query），片段标识符（fragment identifier）
print("【urlsplit】 分解url地址:")
print (parse.urlsplit(url))

# [6] urllib.parse.urlunsplit(parts)
# 结合一个 urlsplit() 返回的元组元素形成一个完整的 URL 字符串。
sr = parse.SplitResult(scheme='http', netloc='www.jb51.net:80', path='/faq.cgi', query='src=fie', fragment='fg')
print("【urlunsplit】 将多个元组元素形成一个完整的 URL 字符串:")
print(parse.urlunsplit(sr))

# [7] urllib.parse.urljoin(base, url, allow_fragments=True)
# 通过将基URL(base )与另一个 URL(url) 组合起来构建完整的（绝对）的URL。
uj1 = parse.urljoin("http://www.asite.com/folder1/currentpage.html","anotherpage.html")
uj2 = parse.urljoin("http://www.asite.com/folder1/currentpage.html","folder2/anotherpage.html")
uj3 = parse.urljoin("http://www.asite.com/folder1/currentpage.html","/folder3/anotnerpage.html")
uj4 = parse.urljoin("http://www.asite.com/folder1/currentpage.html","../finalpage.html")
print("【urljoin】组合url 1：",uj1)
print("【urljoin】组合url 2：",uj2)
print("【urljoin】组合url 3：",uj3)
print("【urljoin】组合url 4：",uj4)

# Note:如果 url 是一个绝对 URL（即以// 或 scheme:// 开头的 url ），url 的主机名或 scheme 将会替代 base 。
uj5 = parse.urljoin("http://www.asite.com/folder/currentpage.html","https://www.python.org/folder2")
uj6 = parse.urljoin("http://www.asite.com/folder/currentpage.html","//www.python.org/folder1")
uj7 = parse.urljoin("http://www.asite.com/folder/currentpage.html","www.python.org/folder2")
print("【urljoin】组合url 5：",uj5)
print("【urljoin】组合url 6：",uj6)
print("【urljoin】组合url 7：",uj7)

# [8] urllib.parse.urldefrag(url)
# 如果 url 包含片段标志符(即 url 尾部的 #+锚点标签 内容），则返回一个不含片段标志符的 url，且片段标志符分成独立的字符串序列。
# 返回值实际上是元组（ tuple）
ud = parse.urldefrag('http://music.163.com/#/my/')
print("【urldefrag】")
print(ud)

# 1.urllib.quote
# [1] urllib.parse.quote(string, safe=’/’, encoding=None, errors=None)
# [1] urllib.parse.quote_from_bytes(bytes, safe=’/’)
# 对字符进行转码,特殊字符（保留字符)，“;” | “/” | “?” | “:” | “@” | “&” | “=” | “+” |”$” | “,” 。
url_asc = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=%E6%95%B0%E5%AD%A6&oq=%25E9%25AB%2598%25E7%25AD%2589%25E6%2595%25B0%25E5%25AD%25A6&rsv_pq=bc3192bd00006199&rsv_t=9874L5kHfiTTvwbjdnArv85fD%2B4yAJXywKFWw1HfLoGCNsctPGieUGbvTcY'
quoted = parse.quote(url_asc)
print('quote:',quoted)

# [2] urllib.parse.quote_plus(string, safe=”, encoding=None, errors=None)
# 与 quote 相似，由 quote_plus 编码 /, quote 不编码 /
p=parse.quote('a&b/c')
print('quote:',p)
plus=parse.quote_plus('a&b/c') 
print('quote_plus：',plus)

# [3] urllib.parse.unquote(string, encoding=’utf-8’, errors=’replace’)
# [3] urllib.parse.unquote_to_bytes(string)
# quote 的逆过程
print(parse.unquote('http%3A//www.baidu.com/doc/sub.html%3Fname%3Dhan%20jian%26age%3D45%40%3B+$'))
print(parse.unquote_to_bytes('http%3A//www.baidu.com/doc/sub.html%3Fname%3Dhan%20jian%26age%3D45%40%3B+$'))

# [4] urllib.parse.unquote_plus(string, encoding=’utf-8’, errors=’replace’)
# quote_plus的逆过程
uq=parse.unquote('1+2')
print('unquote：',uq)
uqp=parse.unquote_plus('1+2')
print('unquote_plus：',uqp)

"""
[5] urllib.parse.urlencode(query, doseq=False, safe=”, encoding=None, errors=None, quote_via=quote_plus)
将字典形式的数据转化成查询字符串
Args:
    query：需要转化的字典数据； 
    doseq： 如果字典的某个值是序列的话是否解析，doseq值为False不解析，值为True的时候解析；
    safe：那些字符串不需要编码； 
    encoding： 要转化成的字符串的编码；
    quote_via：使用quote编码还是qutoe_plus编码，默认quote_plus（也就是空格被转化成+号）
Return:

"""
# 定义要转化的字典数据
qdict = {'age':34,'grils':('lili','tingting'),'name':'han p$'}
print('【urlencode】无参数： ',parse.urlencode(qdict))

print('【urlencode】doseq=True： ',parse.urlencode(qdict,True))

print('【urlencode】doseq=True safe=‘$’： ',parse.urlencode(qdict,True,'$'))

print('【urlencode】doseq=True safe=‘$’ quote_via=quote： ',parse.urlencode(qdict,True,'$',quote_via=parse.quote))

