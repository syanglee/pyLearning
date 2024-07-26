# 查询当前系统所有字体
from matplotlib.font_manager import FontManager as mpl

mpl_fonts = set(f.name for f in mpl().ttflist)

print('all font list get from matplotlib.font_manager:')
for f in sorted(mpl_fonts):
    print('\t' + f)

