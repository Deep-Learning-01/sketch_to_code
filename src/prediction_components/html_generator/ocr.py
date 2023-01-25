from src.exception import SketchtocodeException
from src.logger import logging as lg
import easyocr

import sys


class ApplyOcr:
    def __init__(self, image):

        self.image = image
        self.ocr = easyocr.Reader(['en'],gpu = False)

    def get_ocr_text(self, box):
        """
            Method Name :   get_ocr_text
            Description :   This method returns the text found in the given image.

            Output      :   a string containing the extracted text.
            On Failure  :   Write an exception log and then raise an exception

            Version     :   1.2
            Revisions   :   moved setup to cloud

        """
        try:
            img = self.image[box[1]:box[3], box[0]:box[2]]
            result = self.ocr.readtext(img,detail=0)

            text = " ".join([text for text in result])

            return text
        except Exception as e:
            raise SketchtocodeException(e,sys)




