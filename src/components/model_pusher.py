import os,sys


from src.logger import logging as lg
from src.exception import SketchtocodeException
from src.cloud_storage.aws_syncer import S3Sync
from src.entity.artifact_entity import ModelTrainerArtifact, ModelEvaluationArtifact
from src.entity.config_entity import ModelPusherConfig


class ModelPusher:

    def __init__(self,
                model_trainer_artifact: ModelTrainerArtifact,
                model_evaluation_artifact: ModelEvaluationArtifact):
                

        self.model_trainer_artifact = model_trainer_artifact
        self.model_evaluation_artifact = model_evaluation_artifact
        self.model_pusher_config = ModelPusherConfig()

        self.s3_sync = S3Sync()



    def push_obj_det_model(self):
        """
            Method Name :   push_obj_det_model
            Description :   This method pushes the object detection model to s3 bucket. 

            Output      :   NA
            On Failure  :   Write an exception log and then raise an exception

            Version     :   1.2
            Revisions   :   moved setup to cloud
        """
        try:
            if self.model_evaluation_artifact.is_obj_det_model_accepted:

                #removing existing model in s3
                command = f"aws s3 rm s3://{self.model_pusher_config.obj_detection_s3_model_store_dir_path} --recursive"
                os.system(command)
                lg.info("existing model is removed")

                model_dir = os.path.dirname(self.model_trainer_artifact.obj_detection_trained_model_file_path)
                
                self.s3_sync.sync_folder_to_s3(folder=model_dir, 
                                            aws_folder_path = self.model_pusher_config.obj_detection_s3_model_store_dir_path)
 
        except Exception as e:
            raise SketchtocodeException(e,sys)


    def push_text_det_model(self):
        """
            Method Name :   push_text_det_model
            Description :   This method pushes the text detection model to s3 bucket.

            Output      :   NA
            On Failure  :   Write an exception log and then raise an exception

            Version     :   1.2
            Revisions   :   moved setup to cloud
        """

        try:
            if self.model_evaluation_artifact.is_text_det_model_accepted:

                #removing existing model in s3
                command = f"aws s3 rm s3://{self.model_pusher_config.text_detection_s3_model_store_dir_path}"
                os.system(command)
                lg.info("existing model is removed")

                model_dir = os.path.dirname(self.model_trainer_artifact.text_detection_trained_model_file_path)
                
                self.s3_sync.sync_folder_to_s3(folder=model_dir, 
                                            aws_folder_path = self.model_pusher_config.text_detection_s3_model_store_dir_path)
 
        except Exception as e:
            raise SketchtocodeException(e,sys)


    def initiate_model_pusher(self):
        try:
            lg.info("Model pusher initiated.")
            self.push_obj_det_model()
            self.push_text_det_model()

            lg.info("Model pusher completed successfully.")

             
        except Exception as e:
            raise SketchtocodeException(e,sys)

