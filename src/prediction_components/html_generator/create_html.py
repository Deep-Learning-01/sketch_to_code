from airium import Airium
from src.logger import logging as lg

from src.prediction_components.html_generator.elements import get_elements

from src.exception import SketchtocodeException
import os
import sys
from src.prediction_components.html_generator.ocr import ApplyOcr


class CreateHTML:
    def __init__(self, image):
        self.image = image
        self.add = Airium()
        self.ocr = ApplyOcr(self.image)

    def generate(self, rows):

        """
            Method Name :   generate
            Description :   This method generates a html file.
            Output      :   NA
            On Failure  :   Write an exception log and then raise an exception

            Version     :   1.2
            Revisions   :   moved setup to cloud

        """

        lg.info("Started generating HTML file ")

        try:
            self.add('<!DOCTYPE html>')
            with self.add.html(lang='en'):
                with self.add.head():
                    self.add.meta(charset="utf-8", name='viewport',
                                  content="width=device-width, initial-scale=1, shrink-to-fit=no")
                    self.add.title(_t="HTML")
                    self.add.script(src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js")
                    self.add.script(src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js",
                                    integrity="sha384-oBqDVmMz9ATKxIep9tiCxS/Z9fNfEXiDAYTujMAeBAsjFuCZSmKbSSUnQlmh/jp3",
                                    crossorigin="anonymous")
                    self.add.script(src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.min.js",
                                    integrity="sha384-7VPbUDkoPSGFnVtYi0QogXtr74QeVeeIs99Qfg5YCF+TidwNdjvaKZX19NZ/e6oz",
                                    crossorigin="anonymous")

                    self.add.script(src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js",
                                    integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8",
                                    crossorigin="anonymous")
                    self.add.link(href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css",
                                  rel="stylesheet",
                                  integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT",
                                  crossorigin="anonymous")

                with self.add.body():
                    with self.add.div(klass="container body-content6"):

                        for row in rows:
                            with self.add.div(klass="row justify-content-start", style="padding-top:10px"):
                                for col in row:
                                    with self.add.div(klass="col d-flex flex-column align-items-start",
                                                      style="pself.adding-top:10px;"):
                                        for box in col:
                                            if (box[-1] == 0 or box[-1] == 1 or box[-1] == 3 or box[-1] == 5 or
                                                    box[-1] == 8):
                                                text = self.ocr.get_ocr_text(box)
                                                get_elements(self.add, box[-1], text)
                                                # str(self.add)
                                            else:
                                                last_value = box[-1]
                                                print('box last element', last_value)
                                                get_elements(self.add, box[-1])

            html = str(self.add)
            lg.info("Finished generating HTML File")

            return html

        except Exception as e:
            raise SketchtocodeException(e, sys)
