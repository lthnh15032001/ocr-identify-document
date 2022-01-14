import base64

import cv2
import numpy as np

from vietocr.tool.config import Cfg
from cropper import Cropper
from detector import Detector
from reader import OCR
from .utils import download_weights, Config

# ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# cropper_config_path: str = os.path.join(ROOT_DIR, 'yolov4_tiny.cfg')
# cropper_weight_path: str = os.path.join(
#     ROOT_DIR, 'yolov4_tiny_final.weights')

# detector_config_path: str = os.path.join(ROOT_DIR, 'yolotinyv4_cccd.cfg')
# detector_weight_path: str = os.path.join(
#     ROOT_DIR, 'yolotinyv4_cccd_final.weights')

# reader_weight: str = os.path.join(ROOT_DIR, 'transformerocr.pth')

cfg = Config.load_config()

cropper = Cropper(config_path=download_weights(cfg['cropper']['cfg']),
                  weight_path=download_weights(cfg['cropper']['weight']))

detector = Detector(config_path=download_weights(cfg['detector']['cfg']),
                    weight_path=download_weights(cfg['detector']['weight']))

config = Cfg.load_config_from_name('vgg_transformer')
config['weights'] = cfg['reader']['weight']
config['cnn']['pretrained'] = False
config['device'] = 'cuda:0'
config['predictor']['beamsearch'] = False
reader = OCR(config)


def extract(base64_str: str):
    img_obj = base64.b64decode(base64_str)
    image = cv2.imdecode(np.fromstring(
        img_obj, np.uint8), cv2.IMREAD_COLOR)

    is_card, is_id_card, warped = cropper.process(image=image)

    if is_card is False and is_id_card is None:
        return {'message': 'approved', 'description': 'please upload your id card'}

    if is_id_card is not None and warped is None:
        return {'message': 'approved', 'description': 'please upload id card again'}

    info_images = detector.process(warped)

    info = dict()

    for id in list(info_images.keys()):
        # 7 is id of portrait class
        if id == 7:
            continue
        label = detector.i2label_cc[id]
        if isinstance(info_images[id], np.ndarray):
            info[label] = reader.predict(info_images[id])
        elif isinstance(info_images[id], list):
            info[label] = []
            for i in range(len(info_images[id])):
                info[label].append(reader.predict(info_images[id][i]))

    info['nationality'] = 'Việt Nam'
    if 'sex' in info.keys():
        if 'Na' in info['sex']:
            info['sex'] = 'Nam'
        else:
            info['sex'] = 'Nữ'
    return {'message': 'approved', 'description': 'image is id card', 'info': info}


def bytes_to_information_id_card(img_bytes: bytes):
    m_base64_bytes: bytes = base64.b64encode(img_bytes)
    m_base64_str: str = m_base64_bytes.decode('utf-8')
    print(extract(m_base64_str))
