from PIL import Image
from paddleocr import PaddleOCR, draw_ocr

# paddle_ocr = PaddleOCR(use_angle_cls=True, lang="ch")
# paddle_ocr = PaddleOCR(use_angle_cls=True, lang="ch", det_model_dir="./inference/det/",rec_model_dir="./inference/rec/",cls_model_dir="./inference/cls/")  
paddle_ocr = PaddleOCR()
img_path = r"download/train_ticket_230830.jpg"

result = paddle_ocr.ocr(img_path,cls=True)

for line in result:
    print(line)

result = result[0]
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
im_show = draw_ocr(image, boxes, txts, scores, font_path='doc/fonts/simfang.ttf')
im_show = Image.fromarray(im_show)
im_show.save('download/orc_paddle_4jpg_result.jpg')
