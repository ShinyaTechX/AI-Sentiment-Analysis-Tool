# AI-Sentiment-Analysis-Tool
A production-ready NLP sentiment analysis API using FastAPI, Scikit-learn, and Docker.

# Features
- Text sentiment prediction(positive/negative)
- FastAPI REST API
- Dockerized for deployment
- Clean modular architecture

# Tech Stack
- Python
- FastAPI
- Scikit-learn
- Docker

# Setup
## Local
Bash
pip install -r requirements.txt
python app/model/train.py
uvicorn app.main:app --reload

# Docker
docker-compose up --build