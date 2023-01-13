import sys
from src.exception import SketchtocodeException
from src.logger import logging as lg
from src.utils.html_utils import HtmlUtils
import numpy as np


class TextAlignment:
    def __init__(self):
        self.util = HtmlUtils()

    def check_for_text_bboxes_with_html(self, text_boxes, html_boxes):

        """
            Description: Purpose of this method is to check the overlapping of the text detection bboxes with html elements.
            If the overlapping is above of specified limit then we simply delete that text detection box.
            Conditions we have to check:
                1. Other at bottom right
                2. Other at top right
                3. Other at top left
                4. Other at bottom left
                5. Other at exact right
                6. Other at exact left
                7. Other at exact bottom
                8. Other at exact top
                9. In the middle
            param: boxes, labels, htmlboxes
            return: list
            :type html_boxes: object
        """

        try:
            lg.info("Checking for text bboxes with HTML bboxes...")

            t = 0
            h = 0

            for tbox in range(0, len(text_boxes)):
                h = 0
                for hbox in range(0, len(html_boxes)):

                    # check for bottom right
                    if (
                            html_boxes[h][3] > text_boxes[t][1] > html_boxes[h][1] and text_boxes[t][0] < html_boxes[h][2] <
                            text_boxes[t][2] and text_boxes[t][2] > html_boxes[h][2]):
                        points = [text_boxes[t][3], text_boxes[t][1], html_boxes[h][3], text_boxes[t][1], text_boxes[t][2], text_boxes[t][0],
                                  html_boxes[h][2], text_boxes[t][0]]

                        if self.util.checkDistanceForHTML(points):
                            text_boxes.pop(t)
                            t -= 1
                            break

                    # check for top right
                    elif (text_boxes[t][1] < html_boxes[h][1] and (html_boxes[h][3] > text_boxes[t][3] > html_boxes[h][1]) and
                          (html_boxes[h][0] < text_boxes[t][0] < html_boxes[h][2]) and text_boxes[t][2] > html_boxes[h][2]):
                        points = [text_boxes[t][3], text_boxes[t][1], text_boxes[t][3], html_boxes[h][1], text_boxes[t][2], text_boxes[t][0],
                                  html_boxes[h][2], text_boxes[t][0]]

                        if self.util.checkDistanceForHTML(points):
                            text_boxes.pop(t)
                            t -= 1
                            break

                    # check for top left
                    elif (text_boxes[t][1] < html_boxes[h][1] and (html_boxes[h][3] > text_boxes[t][3] > html_boxes[h][1]) and
                          (html_boxes[h][0] < text_boxes[t][2] < html_boxes[h][2]) and text_boxes[t][0] < html_boxes[h][0]):
                        points = [text_boxes[t][3], text_boxes[t][1], text_boxes[t][3], html_boxes[h][1], text_boxes[t][2], text_boxes[t][0],
                                  text_boxes[t][2], html_boxes[h][0]]

                        if self.util.checkDistanceForHTML(points):
                            text_boxes.pop(t)
                            t -= 1
                            break

                    # check for bottom left
                    elif ((html_boxes[h][0] < text_boxes[t][1] < html_boxes[h][3]) and text_boxes[t][3] > html_boxes[h][3] and
                          text_boxes[t][0] < html_boxes[h][0] and (html_boxes[h][0] < text_boxes[t][2] < html_boxes[h][2])):
                        points = [text_boxes[t][3], text_boxes[t][1], html_boxes[h][3], text_boxes[t][1], text_boxes[t][2], text_boxes[t][0],
                                  text_boxes[t][2], html_boxes[h][0]]

                        if self.util.checkDistanceForHTML(points):
                            text_boxes.pop(t)
                            t -= 1
                            break

                    # check for exact right
                    elif ((html_boxes[h][1] < text_boxes[t][1] < html_boxes[h][3]) and (
                            html_boxes[h][1] < text_boxes[t][3] < html_boxes[h][3]) and
                          (html_boxes[h][0] < text_boxes[t][0] < html_boxes[h][2]) and text_boxes[t][2] > html_boxes[h][2]):
                        points = [text_boxes[t][2], text_boxes[t][0], html_boxes[h][2], text_boxes[t][0]]

                        if self.util.checkDistanceForHTMLExact(points):
                            text_boxes.pop(t)
                            t -= 1
                            break

                    # check for exact left
                    elif (text_boxes[t][0] < html_boxes[h][0] and (html_boxes[h][0] < text_boxes[t][2] < html_boxes[h][2]) and
                          (html_boxes[h][1] < text_boxes[t][1] < html_boxes[h][3]) and (
                                  html_boxes[h][1] < text_boxes[t][3] < html_boxes[h][3])
                          and (html_boxes[h][1] < text_boxes[t][3] < html_boxes[h][3])):
                        points = [text_boxes[t][2], text_boxes[t][0], text_boxes[t][2], html_boxes[h][0]]

                        if self.util.checkDistanceForHTMLExact(points):
                            text_boxes.pop(t)
                            t -= 1
                            break

                    # check for exact bottom
                    elif ((html_boxes[h][0] < text_boxes[t][0] < html_boxes[h][2]) and (
                            html_boxes[h][0] < text_boxes[t][2] < html_boxes[h][2]) and
                          (html_boxes[h][1] < text_boxes[t][1] < html_boxes[h][3]) and html_boxes[h][3] < text_boxes[t][3]):
                        points = [text_boxes[t][3], text_boxes[t][1], html_boxes[h][3], text_boxes[t][1]]

                        if self.util.checkDistanceForHTMLExact(points):
                            text_boxes.pop(t)
                            t -= 1
                            break

                    # check for exact top
                    elif (text_boxes[t][1] < html_boxes[h][1] and (html_boxes[h][1] < text_boxes[t][3] < html_boxes[h][3]) and
                          (html_boxes[h][0] < text_boxes[t][0] < html_boxes[h][2]) and (
                                  html_boxes[h][0] < text_boxes[t][2] < html_boxes[h][2])):
                        points = [text_boxes[t][3], text_boxes[t][1], text_boxes[t][3], html_boxes[h][1]]

                        if self.util.checkDistanceForHTMLExact(points):
                            text_boxes.pop(t)
                            t -= 1
                            break

                    # check in the middle
                    elif ((html_boxes[h][0] < text_boxes[t][0] < html_boxes[h][2]) and (
                            html_boxes[h][0] < text_boxes[t][2] < html_boxes[h][2]) and
                          (html_boxes[h][1] < text_boxes[t][1] < html_boxes[h][3]) and (
                                  html_boxes[h][1] < text_boxes[t][3] < html_boxes[h][3])):
                        text_boxes.pop(t)
                        t -= 1
                        break

                    h += 1
                t += 1

            return text_boxes

        except Exception as e:
            lg.error("Error occurred while checking for text bboxes. ", e)

    def check_for_text_bboxes(self, boxes):
        """
            Description: Purpose of this method is to check the overlapping of the text detection bboxes with other text bboxes.
            If the overlapping is above of specified limit then form the new bbox using their coordinates.
            Conditions we have to check:
                1. Other at bottom right
                2. Other at top right
                3. Other at top left
                4. Other at bottom left
                5. Other at exact right
                6. Other at exact left
                7. Other at exact bottom
                8. Other at exact top
                9. In the middle
            param: boxes, labels, htmlboxes
            return: list
        """

        try:
            lg.info("Checking for text bboxes overlapping...")

            t = 0
            h = 0

            for box in range(0, len(boxes)):
                h = 0
                for nbox in range(0, len(boxes)):
                    if boxes[t][0] == boxes[h][0] and boxes[t][3] == boxes[h][3]:
                        h += 1
                        continue

                    # check for bottom right
                    if boxes[h][3] >= boxes[t][1] >= boxes[h][1] and boxes[t][0] <= boxes[h][2] <= boxes[t][2] and boxes[t][2] >= boxes[h][2]:
                        points = [boxes[t][3], boxes[t][1], boxes[h][3], boxes[t][1], boxes[t][2], boxes[t][0],
                                  boxes[h][2], boxes[t][0], boxes[h][3], boxes[h][1], boxes[h][3], boxes[t][1],
                                  boxes[h][2], boxes[h][0], boxes[t][0], boxes[h][2]]

                        if self.util.checkDistance(points):

                            newOne = [boxes[h][0], boxes[h][1], boxes[t][2], boxes[t][3], 0]
                            boxes.append(np.array(newOne, np.uint16))
                            if h > t:
                                boxes.pop(t)
                                # we have to use h - 1, because after deleting t th element, h might point
                                # element of position one index forward. Same for condition (h < t, i.e t-1)
                                boxes.pop(h - 1)
                            elif h < t:
                                boxes.pop(h)
                                boxes.pop(t - 1)
                            t -= 1
                            break

                    # check for top right
                    if (boxes[t][1] <= boxes[h][1] and (boxes[h][3] >= boxes[t][3] >= boxes[h][1]) and
                            (boxes[h][0] <= boxes[t][0] <= boxes[h][2]) and boxes[t][2] >= boxes[h][2]):
                        points = [boxes[t][3], boxes[t][1], boxes[t][3], boxes[h][1], boxes[t][2], boxes[t][0],
                                  boxes[h][2], boxes[t][0], boxes[h][3], boxes[h][1], boxes[t][3], boxes[h][1],
                                  boxes[h][2], boxes[h][0], boxes[h][2], boxes[t][0]]

                        if self.util.checkDistance(points):

                            newOne = [boxes[h][0], boxes[t][1], boxes[t][2], boxes[h][3], 0]
                            boxes.append(np.array(newOne, np.uint16))
                            if h > t:
                                boxes.pop(t)
                                boxes.pop(h - 1)
                            elif h < t:
                                boxes.pop(h)
                                boxes.pop(t - 1)
                            t -= 1
                            break

                    # check for top left
                    if (boxes[t][1] <= boxes[h][1] and (boxes[h][3] >= boxes[t][3] >= boxes[h][1]) and
                            (boxes[h][0] <= boxes[t][2] <= boxes[h][2]) and boxes[t][0] <= boxes[h][0]):
                        points = [boxes[t][3], boxes[t][1], boxes[t][3], boxes[h][1], boxes[t][2], boxes[t][0],
                                  boxes[t][2], boxes[h][0], boxes[h][3], boxes[h][1], boxes[t][3], boxes[h][1],
                                  boxes[h][2], boxes[h][0], boxes[t][2], boxes[h][0]]

                        if self.util.checkDistance(points):

                            newOne = [boxes[t][0], boxes[t][1], boxes[h][2], boxes[h][3], 0]
                            boxes.append(np.array(newOne, np.uint16))
                            if h > t:
                                boxes.pop(t)
                                boxes.pop(h - 1)
                            elif h < t:
                                boxes.pop(h)
                                boxes.pop(t - 1)
                            t -= 1
                            break

                    # check for bottom left
                    if ((boxes[h][0] <= boxes[t][1] <= boxes[h][3]) and boxes[t][3] >= boxes[h][3] and boxes[t][0] <=
                            boxes[h][0] and (boxes[h][0] <= boxes[t][2] <= boxes[h][2])):
                        points = [boxes[t][3], boxes[t][1], boxes[h][3], boxes[t][1], boxes[t][2], boxes[t][0],
                                  boxes[t][2], boxes[h][0], boxes[h][3], boxes[h][1], boxes[h][3], boxes[t][1],
                                  boxes[h][2], boxes[h][0], boxes[t][2], boxes[h][0]]

                        if self.util.checkDistance(points):

                            newOne = [boxes[t][0], boxes[h][1], boxes[h][2], boxes[t][3], 0]
                            boxes.append(np.array(newOne, np.uint16))
                            if h > t:
                                boxes.pop(t)
                                boxes.pop(h - 1)
                            elif h < t:
                                boxes.pop(h)
                                boxes.pop(t - 1)
                            t -= 1
                            break

                    # check for exact right
                    if ((boxes[h][1] <= boxes[t][1] <= boxes[h][3]) and (boxes[h][1] <= boxes[t][3] <= boxes[h][3]) and
                            (boxes[h][0] <= boxes[t][0] <= boxes[h][2]) and boxes[t][2] >= boxes[h][2]):
                        points = [boxes[h][2], boxes[t][0], boxes[t][2], boxes[t][0], boxes[h][2], boxes[h][0]]

                        if self.util.checkDistanceForExact(points, True):
                            newOne = [boxes[h][0], boxes[h][1], boxes[t][2], boxes[h][3], 0]
                            boxes.append(np.array(newOne, np.uint16))
                            if h > t:
                                boxes.pop(t)
                                boxes.pop(h - 1)
                            elif h < t:
                                boxes.pop(h)
                                boxes.pop(t - 1)
                            t -= 1
                            break

                    # check for exact left
                    if (boxes[t][0] <= boxes[h][0] and (boxes[h][0] <= boxes[t][2] <= boxes[h][2]) and
                            (boxes[h][1] <= boxes[t][1] <= boxes[h][3]) and (
                                    boxes[h][1] <= boxes[t][3] <= boxes[h][3]) and
                            (boxes[h][1] <= boxes[t][3] <= boxes[h][3])):
                        points = [boxes[t][2], boxes[h][0], boxes[t][2], boxes[t][0], boxes[h][2], boxes[h][0]]

                        if self.util.checkDistanceForExact(points, True):
                            newOne = [boxes[t][0], boxes[h][1], boxes[h][2], boxes[h][3], 0]
                            boxes.append(np.array(newOne, np.uint16))
                            if h > t:
                                boxes.pop(t)
                                boxes.pop(h - 1)
                            elif h < t:
                                boxes.pop(h)
                                boxes.pop(t - 1)
                            t -= 1
                            break

                    # check for exact bottom
                    if ((boxes[h][0] <= boxes[t][0] <= boxes[h][2]) and (boxes[h][0] <= boxes[t][2] <= boxes[h][2]) and
                            (boxes[h][1] <= boxes[t][1] <= boxes[h][3]) and boxes[h][3] <= boxes[t][3]):
                        points = [boxes[h][3], boxes[t][1], boxes[t][3], boxes[t][1], boxes[h][3], boxes[h][1]]

                        if self.util.checkDistanceForExact(points):
                            newOne = [boxes[h][0], boxes[h][1], boxes[h][2], boxes[t][3], 0]
                            boxes.append(np.array(newOne, np.uint16))
                            if h > t:
                                boxes.pop(t)
                                boxes.pop(h - 1)
                            elif h < t:
                                boxes.pop(h)
                                boxes.pop(t - 1)
                            t -= 1
                            break

                    # check for exact top
                    if (boxes[t][1] <= boxes[h][1] and (boxes[h][1] <= boxes[t][3] <= boxes[h][3]) and
                            (boxes[h][0] <= boxes[t][0] <= boxes[h][2]) and (
                                    boxes[h][0] <= boxes[t][2] <= boxes[h][2])):
                        points = [boxes[t][3], boxes[h][1], boxes[t][3], boxes[t][1], boxes[h][3], boxes[h][1]]

                        if self.util.checkDistanceForExact(points):
                            newOne = [boxes[h][0], boxes[t][1], boxes[h][2], boxes[h][3], 0]
                            boxes.append(np.array(newOne, np.uint16))
                            if h > t:
                                boxes.pop(t)
                                boxes.pop(h - 1)
                            elif h < t:
                                boxes.pop(h)
                                boxes.pop(t - 1)
                            t -= 1
                            break

                    # check in the middle
                    if ((boxes[h][0] <= boxes[t][0] <= boxes[h][2]) and (boxes[h][0] <= boxes[t][2] <= boxes[h][2]) and
                            (boxes[h][1] <= boxes[t][1] <= boxes[h][3]) and (
                                    boxes[h][1] <= boxes[t][3] <= boxes[h][3])):
                        boxes.pop(t)
                        t -= 1
                        break
                    h += 1
                t += 1

            return boxes

        except Exception as e:
            lg.error("Error occurred while checking for text bboxes. ", e)
