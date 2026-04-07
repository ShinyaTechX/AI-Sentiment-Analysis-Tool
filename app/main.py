from fastapi import FastAPI
from app.schemas.request import SentimentRequest, SentimentResponse
from app.model.predictor import predict_sentiment

app = FastAPI(title="Sentiment Analysis API")

@app.get("/")
def home():
    return {
        "message": "Sentiment API is running"
    }

@app.post("/predict", response_model=SentimentResponse)
def predict(request: SentimentRequest)
    sentiment = predict_sentiment(request.text)
    return SentimentResponse(sentiment=sentiment)