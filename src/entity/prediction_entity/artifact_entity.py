from dataclasses import dataclass 

@dataclass 
class PredictionPipelineArtifact:
    model_weight_file_path: str
    model_config_file_path: str
