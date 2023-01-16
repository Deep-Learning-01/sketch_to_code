from src.exception import SketchtocodeException
from src.logger import logging as lg
import easyocr

import sys


class ApplyOcr:
    def __init__(self, image):

        self.image = image
        self.ocr = easyocr.Reader(['en'],gpu = False)

    def get_ocr_text(self, box):
        try:
            img = self.image[box[1]:box[3], box[0]:box[2]]
            result = self.ocr.readtext(img,detail=0)

            text = " ".join([text for text in result])
            print("text")
            return text
        except Exception as e:
            raise SketchtocodeException(e,sys)




