from urllib import request
import os


# 导入BeautifulSoup
from bs4 import BeautifulSoup as bf

url = "http://www.baidu.com"

# 使用urlopen函数打开一个url，并将返回值赋值给html
html = request.urlopen(url).read()

# 将html转换为字节类型
html_text = bytes.decode(html)

# 打印出html_text
obj = bf(html,'html.parser')

# 从标签head、title里提取标题
title = obj.head.title

# 打印标题
print(title)

# 使用find_all函数获取所有图片的信息
pic_info = obj.find_all('img')
# print("循环遍历所有图片信息")
# print(pic_info)

# 只提取logo图片的信息
logo_pic_info = obj.find_all('img',class_="index-logo-src")
print("循环遍历所有logo图片信息")
for i in logo_pic_info:
    # 分别打印每个图片的信息
    print(i)
# print("输出logo对象")
# print(logo_pic_info)

# 提取第一个logo图片的链接
logo_url = "https:" + logo_pic_info[0]['src']

# 打印链接
print("输出logo url")
print(logo_url)
# logo_url = https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png

# 截取logo路径中最后一个“/”之后的数组元素，如果后面有“?”，将“?”及后面的内容去掉
picName=''.join(logo_url.split('/')[-1].split('?')[0])

print("输出图片名称:")
print(picName)
# 提取logo图片的名称
# logo_title = logo_pic_info[0]['alt']

code_realpath = os.path.dirname(os.path.realpath(__file__))
code_path = os.path.dirname(__file__)
print("real path = ", code_realpath)
print("path = ", code_path)

# # 获取当前待保持图片的路径 TODO: 需要改写为Windows和Linux适配版本
download_path = "d:\MyCloud\MyAliCloud\Workspace\Python\myPy3L\download"
print("download_path = ", download_path)

file_save_path = download_path + '/%s' % picName
print("输出图片保存路径:")
print(file_save_path)

# 使用urlretrieve下载图片
request.urlretrieve(logo_url, file_save_path)





