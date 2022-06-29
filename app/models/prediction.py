from pydantic import BaseModel


class GetPredictionRequest(BaseModel):
    age: int
    gender: int
    height: float
    weight: float
    body_fat_percentage: float
    diastolic: float
    systolonic: float
    gripForce: float
    sit_and_bend_forward_cm: float
    sit_ups_count: float
    broad_jumps: float

class MachineLearningResponse(BaseModel):
    prediction: int


class HealthResponse(BaseModel):
    status: bool
