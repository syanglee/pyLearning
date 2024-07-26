from pikepdf import Pdf,Rectangle
from typing import List
"""
向目标pdf文件批量添加水印
    target_pdf_path:目标pdf文件路径+文件名
    watermark_pad_path:水印pdf文件路径+文件名
    nrow:水印平铺的行数
    ncol:水印平铺的列数
    skip_pages:需要跳过不添加水印的页数
"""

def add_watermark(target_pdf_path:str,
                watermark_pdf_path:str,
                nrow:int,
                ncol:int,
                skip_pages:List[int] = []) -> None:
    #选择需要添加水印的pdf文件
    target_pdf = Pdf.open(target_pdf_path)
    #读取水印 pdf 文件并提取水印
    watermark_pdf = Pdf.open(watermark_pdf_path)
    watermark_page = watermark_pdf.pages[0]
    print("target_pdf_path = ", target_pdf_path)

    #遍历目标 pdf 文件中的所有页，批量添加水印
    for idx,target_page in enumerate(target_pdf.pages):
        #跳过不添加水印的页
        for x in range(ncol):
            for y in range(nrow):
                #向目标页指定范围添加水印
                target_page.add_overlay(watermark_page,     #要在此页面顶部呈现为叠加层的页面或表单 XObject。
                                        # pikepdf.Rectangle目标页面矩形
                                        Rectangle(target_page.trimbox[2] * x / ncol,    # pikepdf.Page.trimbox 获取页面的尺寸
                                                  target_page.trimbox[3] * y / nrow,
                                                  target_page.trimbox[2] * (x + 1) / ncol,
                                                  target_page.trimbox[3] * (y + 1) / nrow))
    #保存PDF文件，同时对pdf文件进行重命名，从文件名倒数第5位写入后缀名
    final_pdf_path = target_pdf_path[:-5] + '_watermark.pdf'
    print("final_pdf_path = ", final_pdf_path)
    target_pdf.save(final_pdf_path)
    print("Had added watermark!")