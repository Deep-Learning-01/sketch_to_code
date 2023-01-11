import os,sys 

from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2 import model_zoo

import numpy as np
from PIL import Image
import cv2

from src.cloud_storage.aws_syncer import S3Sync
from src.exception import SketchtocodeException
from src.logger import logging as lg  
from src.entity.training_entity.config_entity import ModelTrainerConfig
from src.utils import get_prediction_model_config_attribute, get_yaml_file_attributes
from src.entity.prediction_entity.config_entity import PredictionPipelineConfig
from src.entity.prediction_entity.artifact_entity import DetectionArtifact

from src.utils.common import setup_config



class Detection:

    def __init__(self,
                prediction_pipeline_config: PredictionPipelineConfig):

        self.model_trainer_config = ModelTrainerConfig()
        self.model_prediction_config = get_prediction_model_config_attribute()
        self.s3_syncer = S3Sync()
        self.prediction_pipeline_config = prediction_pipeline_config


    def get_model_files_from_s3(self)-> str:

        """
            Method Name :   get_object_detection_data
            Description :   This method downloads the object detection data from s3 bucket
            Output      :   NA
            On Failure  :   Write an exception log and then raise an exception

            Version     :   1.2
            Revisions   :   moved setup to cloud
        """
        try:
            obj_det_model_download_dir = self.prediction_pipeline_config.obj_det_saved_model_dir
            obj_det_s3_model_path = self.prediction_pipeline_config.obj_det_s3_model_path
            self.s3_syncer.sync_folder_from_s3(
                folder = obj_det_model_download_dir,
                aws_folder_path= obj_det_s3_model_path
            )


            text_det_model_download_dir = self.prediction_pipeline_config.text_det_saved_model_dir
            text_det_s3_model_path = self.prediction_pipeline_config.text_det_s3_model_path

            self.s3_syncer.sync_folder_from_s3(
                folder = text_det_model_download_dir,
                aws_folder_path= text_det_s3_model_path
            )

    
        except Exception as e:
            raise SketchtocodeException(e, sys)
        
   
    

    def get_obj_detection_predictions(self,
                        input_image_file,
                        ):
        try:
            config = setup_config(
                trained_model_config_file_path= self.prediction_pipeline_config.obj_det_model_config_path,
                weights_path= self.prediction_pipeline_config.obj_det_model_weight_path
            )
            
            predictor = DefaultPredictor(config)
            output = predictor(input_image_file)

            prediction_boxes = output['instances'].pred_boxes
            prediction_labels = np.array(output['instances'].pred_classes.to("cpu"))+1

            print(f"boxes: {prediction_boxes} \nlabels: {prediction_labels}")

            return prediction_boxes, prediction_labels
            
        except Exception as e:
            raise SketchtocodeException(e,sys)


    def get_text_detection_predictions(self,
                        input_image_file,
                        ):
        try:
            config = setup_config(
                trained_model_config_file_path= self.prediction_pipeline_config.text_det_model_config_path,
                weights_path= self.prediction_pipeline_config.text_det_model_weight_path
            )
            
            predictor = DefaultPredictor(config)
            output = predictor(input_image_file)

            prediction_boxes = output['instances'].pred_boxes
            prediction_labels = np.array(output['instances'].pred_classes.to("cpu"))

            print(f"boxes: {prediction_boxes} \nlabels: {prediction_labels}")

            return prediction_boxes, prediction_labels
            
        except Exception as e:
            raise SketchtocodeException(e,sys)

    

    def initiate_detection(self, input_image_file) -> DetectionArtifact:
        """
            Method Name :   initiate_obj_detection_prediction
            Description :   This method initiates the object detection prediction
            Output      :   NA
            On Failure  :   Write an exception log and then raise an exception

            Version     :   1.2
            Revisions   :   moved setup to cloud

        """
        try:
            self.get_model_files_from_s3()
            obj_det_prediction_boxes, obj_det_prediction_labels = self.get_obj_detection_predictions(input_image_file)
            

            text_det_prediction_boxes, text_det_prediction_labels =  self.get_text_detection_predictions(input_image_file)
            

            detection_artifact = DetectionArtifact(
                obj_det_prediction_boxes= obj_det_prediction_boxes,
                obj_det_prediction_labels= obj_det_prediction_labels,
                text_det_prediction_boxes= text_det_prediction_boxes,
                text_det_prediction_labels= text_det_prediction_labels
            )

            return detection_artifact

        except Exception as e:
            raise SketchtocodeException(e,sys)

