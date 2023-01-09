import os
from src.constant.training_pipeline import *
from src.constant.s3_bucket import *
from src.constant.prediction_pipeline import * 

from dataclasses import dataclass
from datetime import datetime

from from_root import from_root

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
ROOT_DIR: str = from_root()

@dataclass
class TrainingPipelineConfig:
    pipeline_name: str = PIPELINE_NAME
    artifact_dir: str = os.path.join(ROOT_DIR, ARTIFACT_DIR, TRAINING_ARTIFACT_DIR,TIMESTAMP)
    timestamp: str = TIMESTAMP


training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()


@dataclass
class AwsS3Config:
    bucket_name: str = TRAINING_BUCKET_NAME 
    obj_det_path: str = os.path.join(TRAINING_BUCKET_NAME, 
                                        OBJ_DETECTION_FOLDER_NAME)
    text_det_path:str = os.path.join(TRAINING_BUCKET_NAME,
                                        TEXT_DETECTION_FOLDER_NAME)

    obj_det_dataset_path: str = os.path.join( obj_det_path,
                                        DATASET_DIR_NAME)

    
    obj_det_coco_annot_path: str = os.path.join(obj_det_path, COCO_ANNOTATION_FOLDER_NAME)

    text_det_dataset_path: str = os.path.join(text_det_path,
                                        DATASET_DIR_NAME)
    text_det_coco_annot_path: str = os.path.join(text_det_path, COCO_ANNOTATION_FOLDER_NAME)

    obj_det_model_path: str = os.path.join(OBJ_DETECTION_FOLDER_NAME,
                                            MODEL_TRAINER_TRAINED_MODEL_OUTPUT_DIR,
                                            MODEL_TRAINER_TRAINED_MODEL_NAME
                                            )

    text_det_model_path: str = os.path.join(TEXT_DETECTION_FOLDER_NAME,
                                            MODEL_TRAINER_TRAINED_MODEL_OUTPUT_DIR,
                                            MODEL_TRAINER_TRAINED_MODEL_NAME
                                            )
    

    

@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_INGESTION_DIR_NAME)    
    ingested_data_dir: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR)

    object_detection_dir: str  = os.path.join(ingested_data_dir, DATA_INGESTION_OBJ_DET_DIR)
    text_detection_dir: str = os.path.join(ingested_data_dir, DATA_INGESTION_TEXT_DET_DIR)

    object_detection_data_store_dir: str =  os.path.join(object_detection_dir, DATA_INGESTION_DATA_STORE_DIR )
    object_detection_coco_annot_data_store_dir: str = os.path.join( object_detection_dir,DATA_INGESTION_COCO_ANNOT_STORE_DIR )

    text_detection_data_store_dir: str =  os.path.join( text_detection_dir, DATA_INGESTION_DATA_STORE_DIR)
    text_detection_coco_annot_data_store_dir: str = os.path.join( text_detection_dir,DATA_INGESTION_COCO_ANNOT_STORE_DIR )

    #file paths for artifacts
    obj_detection_train_data_dir: str = os.path.join(object_detection_data_store_dir, DATA_INGESTION_TRAIN_DIR)
    obj_detection_test_data_dir: str = os.path.join(object_detection_data_store_dir, DATA_INGESTION_TEST_DIR)

    text_detection_train_data_dir:str = os.path.join(text_detection_data_store_dir, DATA_INGESTION_TRAIN_DIR)
    text_detection_test_data_dir:str = os.path.join(text_detection_data_store_dir, DATA_INGESTION_TEST_DIR)

    obj_detection_train_coco_annot_path:str = os.path.join(object_detection_coco_annot_data_store_dir,
                                                            DATA_INGESTION_TRAIN_COCO_ANNOT_FILE_NAME)
    obj_detection_test_coco_annot_path:str = os.path.join(object_detection_coco_annot_data_store_dir,
                                                            DATA_INGESTION_TEST_COCO_ANNOT_FILE_NAME )
    
    text_detection_train_coco_annot_path:str = os.path.join(text_detection_coco_annot_data_store_dir,
                                                            DATA_INGESTION_TRAIN_COCO_ANNOT_FILE_NAME)      
    
    text_detection_test_coco_annot_path:str = os.path.join(text_detection_coco_annot_data_store_dir,
                                                            DATA_INGESTION_TEST_COCO_ANNOT_FILE_NAME)




    






@dataclass
class ModelTrainerConfig:

    model_trainer_artifact_dir: str = os.path.join(training_pipeline_config.artifact_dir, 
                                                    MODEL_TRAINER_ARTIFACT_DIR_NAME)
    obj_detection_artifact_dir: str = os.path.join(model_trainer_artifact_dir, 
                                                    MODEL_TRAINER_OBJ_DET_ARTIFACT_DIR_NAME)
    text_detection_artifact_dir: str = os.path.join(model_trainer_artifact_dir,
                                                    MODEL_TRAINER_TEXT_DET_ARTIFACT_DIR_NAME )

    #COCO INSTANCE NAMES                                                
    obj_detection_train_coco_ins_name: str = MODEL_TRAINER_OBJ_DET_TRAIN_COCO_INS_NAME
    text_detection_train_coco_ins_name: str = MODEL_TRAINER_TEXT_DET_TRAIN_COCO_INS_DIR

    obj_detection_model_output_dir: str = os.path.join(obj_detection_artifact_dir,
                                                        MODEL_TRAINER_TRAINED_MODEL_OUTPUT_DIR )
    text_detection_model_output_dir: str = os.path.join(text_detection_artifact_dir,
                                                        MODEL_TRAINER_TRAINED_MODEL_OUTPUT_DIR )
    # training configs
   

    obj_detection_training_config_file_path: str = os.path.join(obj_detection_model_output_dir,
                                                            MODEL_TRAINER_TRAINED_MODEL_CONFIG_FILE_NAME)



    text_detection_training_config_file_path: str = os.path.join(text_detection_model_output_dir,
                                                                MODEL_TRAINER_TRAINED_MODEL_CONFIG_FILE_NAME)
                                                

    obj_detection_model_yaml_file_path:str = os.path.join(MODEL_TRAINER_OBJ_DET_MODEL_YAML_FILE_DIR_NAME,
                                                        MODEL_TRAINER_OBJ_DET_MODEL_YAML_CONFIG_FILE_NAME)

    text_detection_model_yaml_file_path: str = os.path.join(ROOT_DIR, MODEL_TRAINER_TEXT_DET_MODEL_YAML_FILE_DIR_NAME,
                                                            MODEL_TRAINER_TEXT_DET_MODEL_YAML_CONFIG_FILE_NAME)

    obj_detection_saved_model_path:str = os.path.join(obj_detection_model_output_dir,
                                                    MODEL_TRAINER_TRAINED_MODEL_NAME ) 
    text_detection_saved_model_path = os.path.join(text_detection_model_output_dir,
                                                     MODEL_TRAINER_TRAINED_MODEL_NAME)

@dataclass
class ModelEvaluationConfig:
    model_eval_artifact_dir = os.path.join(training_pipeline_config.artifact_dir, MODEL_EVALUATION_DIR_NAME)
    
    #s3 configs to download model
    s3_model_key_path: str = MODEL_EVALUATION_BEST_MODEL_NAME
    obj_det_aws_s3_model_dir_path: str = os.path.join( TRAINING_BUCKET_NAME ,
                                                    MODEL_EVALUATION_S3_OBJ_DET_DIR,
                                                    MODEL_EVALUATION_S3_SAVED_MODEL_DIR)


    text_det_aws_s3_model_dir_path: str = os.path.join( TRAINING_BUCKET_NAME,
                                                    MODEL_EVALUATION_S3_TEXT_DET_DIR,
                                                    MODEL_EVALUATION_S3_SAVED_MODEL_DIR
                                                     )



    


    obj_detection_test_coco_ins_name: str = MODEL_EVALUATION_OBJ_DET_TEST_COCO_INS_NAME
    text_detection_test_coco_ins_name: str = MODEL_EVALUATION_TEXT_DET_TEST_COCO_INS_DIR


    obj_det_best_model_dir: str = os.path.join(model_eval_artifact_dir, OBJ_DETECTION_FOLDER_NAME, MODEL_EVALUATION_BEST_MODEL_DIR)
    text_det_best_model_dir: str = os.path.join(model_eval_artifact_dir, TEXT_DETECTION_FOLDER_NAME, MODEL_EVALUATION_BEST_MODEL_DIR)

    obj_det_best_model_path:str = os.path.join(obj_det_best_model_dir, s3_model_key_path)
    text_det_best_model_path:str = os.path.join(text_det_best_model_dir, s3_model_key_path)

    obj_det_best_model_config_file_path:str = os.path.join( obj_det_best_model_dir,
                                                           MODEL_TRAINER_TRAINED_MODEL_CONFIG_FILE_NAME)

    text_det_best_model_config_file_path:str = os.path.join( text_det_best_model_dir,
                                                           MODEL_TRAINER_TRAINED_MODEL_CONFIG_FILE_NAME)

    obj_detection_model_eval_output_dir:str = os.path.join(model_eval_artifact_dir,
                                                            OBJ_DETECTION_FOLDER_NAME,
                                                            MODEL_EVALUATION_OUTPUT_DIR_NAME)


    
    text_detection_model_eval_output_dir:str = os.path.join(model_eval_artifact_dir,
                                                            TEXT_DETECTION_FOLDER_NAME,
                                                            MODEL_EVALUATION_OUTPUT_DIR_NAME)






# @dataclass
# class PredictionPipelineConfig:

#     model_bucket_name = TRAINING_BUCKET_NAME
#     pred_artifact_dir = os.path.join(ARTIFACT_DIR ,PREDICTION_ARTIFACT_DIR,TIMESTAMP)
#     pred_file_input_dir = os.path.join(pred_artifact_dir, PRED_INPUT_FILE_DIR_NAME)
#     pred_model_dir = os.path.join(pred_artifact_dir, PREDICTION_MODEL_DIR_NAME)
#     pred_model_full_path = os.path.join(pred_model_dir, MODEL_TRAINER_TRAINED_MODEL_NAME)


