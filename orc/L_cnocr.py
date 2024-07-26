from cnocr import CnOcr, read_img

# cnocr 一直有问题，系统无法直接下载模型，手动下载后识别还有问题；暂不使用；
img_fp = 'download\train_ticket_230830.jpg'
orc = CnOcr(rec_model_name = 'densenet_lite_136-fc',
            det_model_name = 'db_mobilenet_v3',
            rec_model_backend = 'pytorch',
            det_model_backend = 'pytorch')
result = orc.ocr(img_fp)    # 所有参数都使用默认值
print(result)

