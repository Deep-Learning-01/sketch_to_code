from mmocr.utils.ocr import MMOCR

from src.exception import SketchtocodeException
from src.logger import logging as lg

LEFT_PADDING = 50
RIGHT_PADDING = 50
TOP_PADDING = 50
BOTTOM_PADDING = 50


class ApplyOCR:
    """
        This class is responsible to provide the function to perform Optical Character Recognition.
    """

    def __init__(self, image):
        # self.yamlFile = yamlFile
        self.image = image

        self.ocr = MMOCR(det="PS_CTW", recog="NRTR_1/8-1/4"
                         )

    def get_ocr_text(self, box):

        '''
            This method uses MMOCR to perform ocr on the image text.
            param: list
            return: str
        '''

        try:
            lg.info("Getting OCR in progress...")
            img = self.image[box[1]:box[3], box[0]:box[2]]

            result = self.ocr.readtext(img, print_result=True)
            text = ""

            for results in result[0]['text']:
                text += str(results) + " "

            lg.info("Characters recognized successfully!")
            return text

        except Exception as e:
            lg.error("Error occurred while getting OCR text! ", e)
