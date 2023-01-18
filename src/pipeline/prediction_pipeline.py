from src.logger import logging as lg
from src.exception import SketchtocodeException
from src.prediction_components.detection import Detection
from src.prediction_components.html_generator.generate_html import GenerateHtml
from src.entity.prediction_entity.config_entity import PredictionPipelineConfig
from src.entity.prediction_entity.artifact_entity import DetectionArtifact

import os, sys
import numpy as np
from PIL import Image
import cv2
from fastapi import File
from dataclasses import dataclass


@dataclass
class PredictionPipelineArtifact:
    html_output_file_path: str




class PredictionPipeline:
    def __init__(self):
        self.prediction_pipeline_config = PredictionPipelineConfig()

    def get_image_array(self, image_file: File):
        try:
            image = Image.open(image_file.file)
            image = np.array(image)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = cv2.resize(image, (480, 480))
            return image

        except Exception as e:
            raise SketchtocodeException(e, sys)

    def start_detection(self, image_array: np.array) -> DetectionArtifact:
        try:
            detection = Detection(self.prediction_pipeline_config)
            detection_artifact = detection.initiate_detection(input_image_file=image_array)

            return detection_artifact

        except Exception as e:
            raise SketchtocodeException(e, sys)

    def start_html_generation(self,
                              image_array: np.array,
                              detection_artifact: DetectionArtifact):

        try:
            html_generator = GenerateHtml(
                detection_artifact=detection_artifact,
                image_array=image_array)

            html_output = html_generator.generate_html()

            html_output_file_path = self.prediction_pipeline_config.html_output_file_path

            os.makedirs(
                os.path.dirname(html_output_file_path)
                , exist_ok=True)

            with open(html_output_file_path, "w") as output:
                output.write(html_output)

            lg.info(f"html generation completed. \n The file is saved at: {html_output_file_path}")

        except Exception as e:
            raise SketchtocodeException(e, sys)

    def run_pipeline(self, image_file: File):
        try:
            image_array = self.get_image_array(image_file)
            detection_artifact = self.start_detection(image_array)
            self.start_html_generation(image_array, detection_artifact)
            lg.info(f"pipeline completed. \n The file is saved at: {self}")
            return PredictionPipelineArtifact(html_output_file_path=self.prediction_pipeline_config.html_output_file_path)
        except Exception as e:
            raise SketchtocodeException(e, sys)
