import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

from app.utils.preprocess import clean_text

def train():
    # Example dataset
    data = {
        "text": ["I love this!", "I hate this!", "Amazing product", "Worst ever"],
        "label": [1, 0, 1, 0]
    }

    df = pd.DataFrame(data)
    # df = pd.read_csv("data/dataset.csv", encoding="latin-1")
    df["text"] = df["text"].apply(clean_text)

    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("clf", LogisticRegression())
    ])

    pipeline.fit(df["text"], df["label"])

    joblib.dump(pipeline, "sentiment_model.joblib")
    print("Model saved!")

if __name__ == "__main__":
    train()