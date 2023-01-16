import numpy as np

from src.exception import SketchtocodeException
from src.exception import SketchtocodeException
from src.logger import logging as lg
from src.entity.prediction_entity.artifact_entity import DetectionArtifact
from src.utils.html_utils import HtmlUtils
from src.prediction_components.html_generator.text_process import TextAlignment
from src.prediction_components.html_generator.create_html import CreateHTML

import sys


class GenerateHtml:
    def __init__(self,
                 detection_artifact: DetectionArtifact,
                 image_array):

        self.detection_artifact = detection_artifact
        self.text_process = TextAlignment()
        self.utils = HtmlUtils()
        self.create_html = CreateHTML(image_array)

    def get_boxes(self):
        try:

            # object detection
            detection_box = np.array(self.detection_artifact.obj_det_prediction_boxes.to("cpu"))
            detection_labels = self.detection_artifact.obj_det_prediction_labels

            boxes = []

            for b in range(0, len(detection_box)):
                boxes.append(np.append(np.array(detection_box[b].to("cpu"), np.uint16), detection_labels[b]))

            # text detection
            text_detection_box = np.array(self.detection_artifact.text_det_prediction_boxes.to("cpu"))
            text_detection_labels = self.detection_artifact.text_det_prediction_labels

            boxes_text = []

            for b in range(0, len(text_detection_box)):
                boxes_text.append(np.append(np.array(text_detection_box[b].to("cpu"), np.uint16), 0))

            return boxes, boxes_text

        except Exception as e:
            raise SketchtocodeException(e, sys)

    def create_text_boxes_with_html(self):
        try:
            boxes, boxes_text = self.get_boxes()
            boxes_text = self.text_process.check_for_text_bboxes_with_html(boxes_text, boxes)
            boxes_text = self.text_process.check_for_text_bboxes(boxes_text)

            for i in boxes_text:
                boxes.append(i)

            return boxes

        except Exception as e:
            raise SketchtocodeException(e, sys)

    def get_html_rows_and_columns(self, boxes):
        """
            Method Name :   get_html_rows_and_columns
            Description :   This method returns a list of rows and columns

            Output      :   a list of rows and columns
            On Failure  :   Write an exception log and then raise an exception

            Version     :   1.2
            Revisions   :   moved setup to cloud

        """

        try:
            rows = [[], [], [], []]

            for box in boxes:
                box = np.array(box)

                row_num1 = self.utils.getRowNumber(box[1])  # get for y1
                row_num2 = self.utils.getRowNumber(box[3])  # get for y2

                row = self.utils.getActualRowNumber(row_num1, row_num2, box)

                if len(rows[row]) == 0:
                    rows[row].append([box])
                else:

                    inserted = False
                    for col in range(len(rows[row])):

                        for elm in range(len(rows[row][col])):

                            e = rows[row][col][elm]
                            if ((((box[0] < e[0]) and (box[2] < e[2]) and (box[2] > e[0])) or
                                 ((box[0] > e[0]) and (box[2] > e[2]) and (box[0] < e[2])) or
                                 ((box[0] > e[0]) and (box[2] < e[2])) or
                                 ((box[0] < e[0]) and (box[2] > e[2])))):
                                rows[row][col].append(box)
                                rows[row][col] = sorted(rows[row][col], key=lambda x: x[1])
                                inserted = True
                                break

                        if inserted:
                            break
                        else:
                            if col == len(rows[row]) - 1:
                                # check if we are at last column
                                rows[row].append([box])
                                inserted = True
                                break

            rows_new = self.utils.sortColumns(rows)
            lg.info("Calculated rows and columns all the Bboxes")
            return rows_new

        except Exception as e:
            raise SketchtocodeException(e, sys)

    def generate_html(self):
        try:
            boxes = self.create_text_boxes_with_html()

            rows = self.get_html_rows_and_columns(boxes)
            print(rows)

            html_output = self.create_html.generate(rows)

            return html_output

        except Exception as e:
            raise SketchtocodeException(e, sys)
