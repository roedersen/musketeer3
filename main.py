import transformers 
import torch
import torchvision
import torchaudio
from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

sentiment_model = pipeline("sentiment-analysis")

# sentiment_query_sentence = get_random_comment(top_comments)
# sentiment = sentiment_model(sentiment_query_sentence)
# print(f"Sentiment test: {sentiment_query_sentence} == {sentiment})

from pydantic import BaseModel

class PredictionRequest(BaseModel):
  query_string: str
  

@app.post("/prediction")
def my_endpoint(request: PredictionRequest):
  # YOUR CODE GOES HERE
  sentiment = sentiment_model(request.query_string)
  return (f"Sentiment test: {request.query_string} == {sentiment}")
