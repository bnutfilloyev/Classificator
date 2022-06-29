from typing import Any, List

import joblib
from core.errors import PredictException
from fastapi import APIRouter, HTTPException
from loguru import logger
from models.prediction import GetPredictionRequest, MachineLearningResponse
from services.predict import MachineLearningModelHandlerScore as model

router = APIRouter()

get_prediction = lambda data_input: model.predict(data_input, load_wrapper=joblib.load)



@router.get("/predict", response_model=MachineLearningResponse, name="predict:get-data")
async def predict(data_input: GetPredictionRequest):
    input_data = data_input.dict()
    data_input = list(input_data.values())

    if not data_input:
        raise HTTPException(status_code=404, detail=f"'data_input' argument invalid!")
    try:
        print(get_prediction(data_input))
        prediction = get_prediction(data_input)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Exception: {e}")

    return MachineLearningResponse(prediction=prediction)