import joblib

from config import MODEL_PATH

def predict(sample):

    model = joblib.load(MODEL_PATH)

    prediction = model.predict(sample)

    return prediction
