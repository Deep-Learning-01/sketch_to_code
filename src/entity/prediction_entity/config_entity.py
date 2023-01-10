from dataclasses import dataclass

from src.constant.prediction_pipeline import *
from src.constant.training_pipeline import *
import os,sys
from datetime import datetime

from from_root import from_root

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
ROOT_DIR: str = from_root()



@dataclass 
class AwsS3Config:
    s3_model_key_path: str = MODEL_TRAINER_TRAINED_MODEL_NAME
    obj_det_aws_s3_model_dir_path: str = os.path.join( TRAINING_BUCKET_NAME ,
                                                    MODEL_EVALUATION_S3_OBJ_DET_DIR,
                                                    MODEL_EVALUATION_S3_SAVED_MODEL_DIR)


    text_det_aws_s3_model_dir_path: str = os.path.join( TRAINING_BUCKET_NAME,
                                                    MODEL_EVALUATION_S3_TEXT_DET_DIR,
                                                    MODEL_EVALUATION_S3_SAVED_MODEL_DIR
                                                     )



aws_s3_config: AwsS3Config = AwsS3Config()

@dataclass
class PredictionPipelineConfig:
    artifact_dir: str = os.path.join(ROOT_DIR, ARTIFACT_DIR, PREDICTION_ARTIFACT_DIR,TIMESTAMP)
   


training_pipeline_config: PredictionPipelineConfig = PredictionPipelineConfig()


@dataclass
class PredictionPipelineConfig:

    obj_det_s3_model_path: str = os.path.join( TRAINING_BUCKET_NAME,
                                            S3_OBJ_DET_DIR)


    text_det_s3_model_path: str = os.path.join( TRAINING_BUCKET_NAME,
                                                S3_TEXT_DET_DIR)



    obj_det_artifact_dir = os.path.join( training_pipeline_config.artifact_dir,
                                                S3_OBJ_DET_DIR )

    text_det_artifact_dir = os.path.join( training_pipeline_config.artifact_dir,
                                                S3_TEXT_DET_DIR )



    obj_det_saved_model_dir: str = os.path.join(obj_det_artifact_dir,
                                            MODEL_TRAINER_TRAINED_MODEL_OUTPUT_DIR ) 



    text_det_saved_model_dir: str = os.path.join(text_det_artifact_dir,
                                            MODEL_TRAINER_TRAINED_MODEL_OUTPUT_DIR ) 

    obj_det_model_weight_path: str = os.path.join( obj_det_saved_model_dir,
    MODEL_TRAINER_TRAINED_MODEL_NAME)

    text_det_model_weight_path: str = os.path.join( text_det_saved_model_dir,
    MODEL_TRAINER_TRAINED_MODEL_NAME ) 


    obj_det_model_config_path: str = os.path.join( obj_det_saved_model_dir,
    MODEL_TRAINER_TRAINED_MODEL_NAME)

    text_det_model_config_path: str = os.path.join( text_det_saved_model_dir,
    MODEL_TRAINER_TRAINED_MODEL_NAME ) 

    