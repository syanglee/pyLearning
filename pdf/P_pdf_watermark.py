from P_reportlab_create_watermark import create_watermark
from P_pikepdf_add_watermark import add_watermark
from reportlab.pdfbase import pdfmetrics

watermark_content = '鼎信诺内部资料，涉密文件，严谨外传！'
watermark_temp_file_name = "test"
target_file_name = "DXN_IAMS_Product_White_Papers"

watermark_temp_file_path = create_watermark(
    watermark_content=watermark_content,
    file_name=watermark_temp_file_name,
    width=200,
    height=200,
    font_size=35,
    angle=45,
    text_fill_alpha=0.3)

add_watermark(
    target_pdf_path='download/{}.pdf'.format(target_file_name),
    watermark_pdf_path=watermark_temp_file_path,
    nrow=2,
    ncol=1,
    skip_pages=[0]
)