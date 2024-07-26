from paddleocr import PaddleOCR, draw_ocr

# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
paddle_ocr = PaddleOCR(use_angle_cls=True, lang="ch", page_num=2)
img_path = r"download/dinner_230830.pdf"

result = paddle_ocr.ocr(img_path,cls=True)

for idx in range(len(result)):
    res = result[idx]
    for line in res:
        print(line)

# 显示结果
import fitz
from PIL import Image
import cv2
import numpy as np
imgs = []
with fitz.open(img_path) as pdf:
    # PyMuPDF 升级到1.9之后，很多属性参数和方法都改了，其中，将 pageCount 属性改为 page_count
    for pg in range(0, pdf.page_count):
        page = pdf[pg]
        mat = fitz.Matrix(2, 2)
        # PyMuPDF 升级到1.9之后，将 getPixmap() 改为 get_pixmap()
        pm = page.get_pixmap(matrix=mat, alpha=False)
        # if width or height > 2000 pixels, don't enlarge the image
        if pm.width > 2000 or pm.height > 2000:
            pm = page.get_pixmap(matrix=fitz.Matrix(1, 1), alpha=False)
        
        img = Image.frombytes("RGB", [pm.width, pm.height], pm.samples)
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        imgs.append(img)

for idx in range(len(result)):
    res = result[idx]
    image = imgs[idx]
    boxes = [line[0] for line in res]
    txts = [line[1][0] for line in res]
    scores = [line[1][1] for line in res]
    im_show = draw_ocr(image, boxes, txts, scores, font_path='doc/fonts/simfang.ttf')
    im_show = Image.fromarray(im_show)
    im_show.save('download/orc_paddle_4pdf_result{}.jpg'.format(idx))
