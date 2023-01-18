from fastapi import FastAPI, Request, File, UploadFile
import shutil
import sys
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from uvicorn import run as app_run
from starlette.responses import FileResponse
from fastapi.templating import Jinja2Templates

from src.pipeline.training_pipeline import TrainingPipeline
from src.pipeline.prediction_pipeline import PredictionPipeline
from src.exception import SketchtocodeException
from src.logger import logging as lg
from src.logger import *
from src.constant.application import *

app = FastAPI()

origins = ["*"]

templates = Jinja2Templates(directory='templates')

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/train")
async def trainRouteClient():
    try:
        train_pipeline = TrainingPipeline()

        train_pipeline.run_pipeline()
        lg.info("training successfully completed.")

        return Response("Training successful !!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")


@app.post("/generate_html")
def predict_from_video_file(file: UploadFile = File(...)):
    try:
        pred_pipeline = PredictionPipeline()
        prediction_pipeline_artifact = pred_pipeline.run_pipeline(file)
        output_file_path = prediction_pipeline_artifact.html_output_file_path
        return FileResponse(output_file_path, media_type='application/octet-stream',
                            filename=os.path.basename(output_file_path))


    except Exception as e:
        raise SketchtocodeException(e, sys)





@app.post("/logs")
def predict():
    try:
        return FileResponse(LOG_FILE_PATH, media_type='application/octet-stream', filename=LOG_FILE)

    except Exception as e:
        raise SketchtocodeException(e, sys)


if __name__ == "__main__":
    app_run(app, host=APP_HOST, port=APP_PORT)