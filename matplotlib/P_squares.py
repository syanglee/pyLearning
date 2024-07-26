import matplotlib as mpl
mpl.use('TkAgg')
# 获得matplotlib包所在文件夹，matplotlibrc为修改matplotlib字体的设置文件
print(mpl.matplotlib_fname())   # /root/crawler_env/lib/python3.8/site-packages/matplotlib/mpl-data/matplotlibrc
# 获得matplotlib缓存目录地址
print(mpl.get_cachedir())   # /root/.cache/matplotlib，清除该文件夹可以重新加载字体

import matplotlib.pyplot as plt

squares = [-1,4,9,16,25]
# 在一张图片中绘制一个或多个图表
fig,ax = plt.subplots()
# 绘制，linewidth设置线条的粗细
ax.plot(squares,linewidth=3)
# 设置图表标题
ax.set_title("平方数", fontsize=24)
# 设置x轴坐标标签
ax.set_xlabel("值", fontsize=14)
# 设置y轴坐标标签
ax.set_ylabel("值的平方", fontsize=14)
# 设置刻度标记大小
ax.tick_params(axis='both', labelsize=14)
# 打开Matplotlib查看器，并显示绘制的图表
plt.show()