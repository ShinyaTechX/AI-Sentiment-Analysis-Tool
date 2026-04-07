import joblib
from app.utils.preprocess import clean_text

model = joblib.load("sentiment_model.joblib")

def predict_sentiment(text: str) -> str:
    cleaned = clean_text(text)
    prediction = model.predict([cleaned])[0]
    return "positive" if prediction == 1 else "negative"