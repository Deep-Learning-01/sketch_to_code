from dataclasses import dataclass 
from numpy import array


@dataclass 
class DetectionArtifact:
    obj_det_prediction_boxes: array
    obj_det_prediction_labels: array
    text_det_prediction_boxes: array
    text_det_prediction_labels: array
