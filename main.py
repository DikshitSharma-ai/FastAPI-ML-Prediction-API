
# ============================================
# main.py
# ============================================

import time
from contextlib import asynccontextmanager

import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

pipeline = None


# ============================================
# Load ML Model
# ============================================

@asynccontextmanager
async def lifespan(app: FastAPI):
    global pipeline

    pipeline = joblib.load("model.pkl")

    yield


app = FastAPI(lifespan=lifespan)


# ============================================
# Input Schema
# ============================================

class EmployeeInput(BaseModel):
    age: int
    salary: float


# ============================================
# Latency Middleware
# ============================================

@app.middleware("http")
async def measure_latency(request, call_next):

    start_time = time.time()

    response = await call_next(request)

    end_time = time.time()

    latency = end_time - start_time

    print(f"{request.method} {request.url.path} - {latency:.4f} seconds")

    return response


# ============================================
# Health Check
# ============================================

@app.get("/health")
def health():

    return {
        "status": "ok"
    }


# ============================================
# Readiness Check
# ============================================

@app.get("/ready")
def ready():

    if pipeline is None:
        raise HTTPException(
            status_code=503,
            detail="model is not ready"
        )

    return {
        "status": "ready"
    }


# ============================================
# Single Prediction
# ============================================

@app.post("/predict")
def predict(data: EmployeeInput):

    if pipeline is None:
        raise HTTPException(
            status_code=503,
            detail="model is not ready"
        )

    input_data = [[data.age, data.salary]]

    prediction = pipeline.predict(input_data)

    return {
        "prediction": int(prediction[0])
    }


# ============================================
# Batch Prediction
# ============================================

@app.post("/predict_batch")
def predict_batch(data: list[EmployeeInput]):

    if pipeline is None:
        raise HTTPException(
            status_code=503,
            detail="model is not ready"
        )

    input_data = [
        [employee.age, employee.salary]
        for employee in data
    ]

    predictions = pipeline.predict(input_data)

    return {
        "predictions": predictions.tolist()
    }
