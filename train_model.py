# ============================================
# train_model.py
# ============================================

import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

x = [
    [20, 20000],
    [22, 25000],
    [25, 30000],
    [28, 35000],
    [30, 40000],
    [32, 45000],
    [35, 50000],
    [38, 55000]
]

y = [0, 0, 0, 0, 1, 1, 1, 1]


pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])


pipeline.fit(x, y)

joblib.dump(pipeline, "model.pkl")

print("model saved successfully")
