from pathlib import Path
import joblib

# project root directory 
BASE_DIR = Path(__file__).resolve().parent.parent

# model file path
MODEL_PATH = BASE_DIR / "model.pkl"

# test1: check model file 
def test_model_file_exists():
    assert MODEL_PATH.exists()

# test2: check model loading
def test_model_loading():
    model = joblib.load(MODEL_PATH)
    assert model is not None 

# test3: check model prediction 
def test_model_prediction():
    model = joblib.load(MODEL_PATH)

    # DUMMY input matching train_model.py format: [[age,salary]] 
    dummy_input = [[25,30000]]
    prediction = model.predict(dummy_input)
    assert len(prediction) == 1
    assert prediction[0] in [0,1]
