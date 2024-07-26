from typing import Union, Tuple
from reportlab.lib import units
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics

# 查看 reportlab 已注册的字体
print(pdfmetrics.getRegisteredFontNames())
print(pdfmetrics.dumpFontData())

TTF_FONT = "msyh"
CID_FONT = "STSong-Light"

from reportlab.pdfbase.cidfonts import UnicodeCIDFont  
pdfmetrics.registerFont(UnicodeCIDFont(CID_FONT))

#from reportlab.pdfbase.ttfonts import TTFont
#pdfmetrics.registerFont(TTFont(TTF_FONT, '{}.ttf'.format(TTF_FONT)))


"""
用于生成包含content文字内容的水印pdf文件

    watermark_content: 水印文本内容
    file_name: 导出的水印文件名
    c_width: 画布宽度，单位：mm
    c_height: 画布高度，单位：mm
    font: 对应注册的字体代号
    fontsize: 字号大小
    angle: 旋转角度
    text_stroke_color_rgb: 文字轮廓rgb色
    text_fill_color_rgb: 文字填充rgb色
    text_fill_alpha: 文字透明度
"""
def create_watermark(watermark_content: str,
                    file_name: str,
                    width: Union[int, float],
                    height: Union[int, float],
                    font: str = CID_FONT,
                    font_size: Union[int, float] = 35,
                    angle: Union[int, float] = 45,
                    text_stroke_color_rgb: Tuple[int, int, int] = (0, 0, 0), # 文本字符的笔画颜色
                    text_fill_color_rgb: Tuple[int, int, int] = (0, 0, 0),   # 文本字符的填充颜色
                    text_fill_alpha: Union[int, float] = 1) -> None:
    
    watermark_file_path = 'download/temp_watermark_{}.pdf'.format(file_name)
    print("watermark_file_path = ",watermark_file_path)

    # 创建PDF 文件，指定文件名、尺寸，以像素为单位
    c = canvas.Canvas(watermark_file_path, pagesize=(width * units.mm, height * units.mm))
    
    # 将水印文本移动到画布中心
    c.translate(width * 0.1 * units.mm, height * 0.1 * units.mm)

    # 旋转画布
    c.rotate(angle)

    # 设置字体
    c.setFont(font, font_size)
    
    # 设置文字轮廓颜色
    c.setStrokeColorRGB(*text_stroke_color_rgb)

    # 设置文字填充颜色
    c.setFillColorRGB(*text_fill_color_rgb)

    # 设置文字填充透明度
    c.setFillAlpha(text_fill_alpha)

    # 绘制文字
    c.drawString(0, 0, watermark_content)

    # 将画布保存
    c.save()

    return watermark_file_path

