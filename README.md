FastAPI ML Prediction API
A beginner-friendly Machine Learning model serving project built using FastAPI.

This project demonstrates how a trained ML model can be exposed through a REST API and used to generate predictions through Swagger UI.

Project Architecture
Client
  |
  v
FastAPI REST API
  |
  v
Pydantic Validation
  |
  v
Preprocessing Pipeline
  |
  v
ML Model
  |
  v
Prediction
  |
  v
JSON Response
Endpoints
GET  /health
GET  /ready
POST /predict
POST /predict_batch
Swagger UI
Run the API:

uvicorn main:app --reload
Open:

http://127.0.0.1:8000/docs
Swagger UI acts as the client. Select an endpoint, click Try it out, enter JSON data, and click Execute to send the request and view the response.

Example
POST /predict
Request:

{
    "age": 30,
    "salary": 40000
}
Response:

{
    "prediction": 1
}
POST /predict_batch
Request:

[
    {
        "age": 22,
        "salary": 25000
    },
    {
        "age": 30,
        "salary": 40000
    }
]
Response:

{
    "predictions": [0, 1]
}
Features
FastAPI REST API
Pydantic validation
ML model loading
Preprocessing pipeline
Single and batch prediction
Health and readiness checks
Error handling
Latency measurement
Swagger/OpenAPI
Technologies
Python • FastAPI • Pydantic • Scikit-learn • Uvicorn • Joblib