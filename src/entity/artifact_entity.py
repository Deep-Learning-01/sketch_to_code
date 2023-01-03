from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    training_folder_path:str 
    test_folder_path:str 


@dataclass
class ModelTrainerArtifact:
    trained_model_file_path:str 
@dataclass
class ModelEvaluationArtifact:
    is_model_accepted:bool
    trained_model_dir:str 



@dataclass
class ModelPusherArtifact:
    bucket_name:str
    s3_model_path:str 


    
