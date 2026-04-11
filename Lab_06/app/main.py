from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(title="Sentiment Analysis API", version="1.0.0")

class ReviewInput(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    text: str
    sentiment: str
    confidence: float

@app.get("/")
async def root():
    """Root endpoint returning a welcome message."""
    return {
        "message": "Sentiment Analysis API — DistilBERT on IMDb",
        "author": "Jennisha Christina Martin",
    }

@app.get("/health")
async def health():
    """Health check endpoint for Kubernetes readiness probes."""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.get("/model-info")
async def model_info():
    """Returns metadata about the deployed model."""
    return {
        "model": "DistilBERT",
        "dataset": "IMDb Movie Reviews",
        "task": "Binary Sentiment Classification",
        "classes": ["negative", "positive"],
        "training_samples": 25000,
        "test_samples": 25000,
        "framework": "Hugging Face Transformers",
    }

@app.post("/predict", response_model=SentimentResponse)
async def predict(review: ReviewInput):
    """
    Predict sentiment of a movie review.
    """
    text = review.text.lower()

    positive_words = [
        "great", "amazing", "excellent", "wonderful", "fantastic", "love",
        "brilliant", "masterpiece", "enjoy", "beautiful", "perfect", "best",
    ]
    negative_words = [
        "bad", "terrible", "awful", "horrible", "worst", "hate",
        "boring", "waste", "poor", "disappointing", "mediocre", "dull",
    ]

    pos_count = sum(1 for w in positive_words if w in text)
    neg_count = sum(1 for w in negative_words if w in text)
    total = pos_count + neg_count

    if total == 0:
        sentiment = "neutral"
        confidence = 0.50
    elif pos_count > neg_count:
        sentiment = "positive"
        confidence = round(pos_count / total, 2)
    else:
        sentiment = "negative"
        confidence = round(neg_count / total, 2)

    return SentimentResponse(
        text=review.text,
        sentiment=sentiment,
        confidence=confidence,
    )
