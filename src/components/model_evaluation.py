import os,sys
from src.logger import logging as lg
from src.exception import SketchtocodeException
from src.entity.artifact_entity import ModelEvaluationArtifact, ModelTrainerArtifact, DataIngestionArtifact

from src.entity.config_entity import ModelEvaluationConfig
from src.cloud_storage.aws_syncer import S3Sync


class ModelEvaluation:

    def __init__(self,
                data_ingestion_artifact: DataIngestionArtifact,
                model_trainer_artifact: ModelTrainerArtifact ):


        self.model_eval_config = ModelEvaluationConfig()
        self.model_trainer_artifact = model_trainer_artifact
        self.data_ingestion_artifact = data_ingestion_artifact
        self.s3_sync = S3Sync()

    def get_best_model_from_s3(self):
        """
            Method Name :   get_best_model_from_s3
            Description :   This method downloads the best model from the s3
                            and returns the best model object. 

            Output      :   best model object
            On Failure  :   Write an exception log and then raise an exception

            Version     :   1.2
            Revisions   :   moved setup to cloud
        """
        try:
            obj_det_s3_model_path = self.model_eval_config.obj_det_aws_s3_model_path
            best_model_dir = self.model_eval_config.obj_det_best_model_dir
            self.s3_sync.sync_folder_from_s3(aws_file_path= obj_det_s3_model_path,
            folder= best_model_dir )

            print("model downloaded.")
             
        except Exception as e:
            raise SketchtocodeException(e,sys)

    def evaluate_trained_model(self):
        """
            Method Name :   evaluate_trained_model
            Description :   This method evaluates the trained model stored in artifacts.

            Output      :   trained model evaluation metric
            On Failure  :   Write an exception log and then raise an exception

            Version     :   1.2
            Revisions   :   moved setup to cloud
        """
        try:
            pass
        except Exception as e:
            raise SketchtocodeException(e,sys)

    def evaluate_best_model(self):
        """
            Method Name :   evaluate_best_model
            Description :   This method evaluates the best model stored in s3.

            Output      :   best model evaluation metric
            On Failure  :   Write an exception log and then raise an exception

            Version     :   1.2
            Revisions   :   moved setup to cloud
        """
        try:
            pass
        except Exception as e:
            raise SketchtocodeException(e,sys)

    def initiate_evaluation(self):
        """
            Method Name :   initiate_evaluation
            Description :   This method initiated the model evaluation component of the training pipeline. 

            Output      :   model evaluation artifact
            On Failure  :   Write an exception log and then raise an exception

            Version     :   1.2
            Revisions   :   moved setup to cloud
        """
        try:
            pass
        except Exception as e:
            raise SketchtocodeException(e,sys)
