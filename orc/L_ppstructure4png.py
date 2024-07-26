from paddleocr import PPStructure, draw_structure_result, save_structure_res
from PIL import Image
import cv2, os

"""
PPStructure
    show_log:                   默认为 False, True 开启日志, False 关闭日志
    image_orientation:          是否执行图像方向分类; 默认为 False, True 开启图像方向分类, 开启表格识别, False 关闭图像方向分类    
    table:                      是否执行表格识别; 默认为 True, True 开启表格识别, False 关闭表格识别
    merge_no_span_structure:    表格识别模型中，是否对'<td>'和'</td>' 进行合并; 默认为 False, True 合并, False 不合并
    layout：                    是否执行版面分析; 默认为 True, True 开启版面分析, False 关闭版面分析
    ocr:                        对于版面分析中的非表格区域，是否执行ocr; 默认为 True, True 开启ocr扫描, False 关闭ocr扫描
    recovery:                   是否执行版面恢复; 默认为 False, True 开启版面恢复, False 关闭版面恢复
    save_pdf:                   版面恢复导出docx文件的同时，是否导出pdf文件; 默认为 False, True 开启导出pdf文件, False 关闭导出pdf文件
    structure_version:          模型版本; 默认为 PP-structure， 可选 PP-structure和PP-structurev2
    lang：                      语言选择; 默认为 ch, 支持的多语言语种：`ch`, `en`, `fr`, `german`, `korean`, `japan`
    output:                     结果保存地址; 默认为 ./output/table
    mode:                       模型类型选择; 默认为 structure, 可选 structure, kie

    图像方向分类+版面分析+表格识别  PPStructure(show_log=True, image_orientation=True)
    版面分析+表格识别              PPStructure(show_log=True)
    版面分析                      PPStructure(table=False, ocr=False, show_log=True)
    表格识别                      PPStructure(layout=False, show_log=True)
    （英文）版面恢复               PPStructure(recovery=True, lang='en')

"""

table_engine = PPStructure(show_log=True)

# 保存结果文件夹地址 
save_folder = "./download"
# 待识别图片的全路径
img_path = "./download/invoice_230830.png"
# PaddleOCR下提供字体包路径
font_path_ = "./doc/fonts/simfang.ttf"

img = cv2.imread(img_path)

result = table_engine(img)
# 将待识别图和识别结果保存到结果文件夹下
# os.path.basename(img_path).split('.')[0] 以待识别图片的文件名为文件夹，进行保存
save_structure_res(result, save_folder,os.path.basename(img_path).split('.')[0])

for line in result:
    line.pop('img')
    # print(line)

image = Image.open(img_path).convert('RGB')

im_show = draw_structure_result(image, result, font_path=font_path_)
im_show = Image.fromarray(im_show)
im_show.save('./download/orc_ppstructure_4jpg_result.jpg')


