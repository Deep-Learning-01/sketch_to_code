from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    obj_detection_training_data_folder_path: str
    obj_detection_testing_data_folder_path: str
    obj_detection_coco_train_annot_path: str
    obj_detection_coco_test_annot_path: str

    text_detection_training_data_folder_path: str
    text_detection_testing_data_folder_path: str
    text_detection_coco_train_annot_path: str
    text_detection_coco_test_annot_path: str



@dataclass
class ModelTrainerArtifact:
    obj_detection_trained_model_file_path:str 
    text_detection_trained_model_file_path:str
    obj_detection_trained_model_config_file_path:str
    text_detection_trained_model_config_file_path:str
@dataclass
class ModelEvaluationArtifact:
    is_obj_det_model_accepted:bool
    is_text_det_model_accepted: bool
    # trained_model_dir:str 



@dataclass
class ModelPusherArtifact:
    bucket_name:str
    s3_model_path:str 


    
