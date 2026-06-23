from fastapi import FastAPI
from pydantic import BaseModel
from model import predict
#from transformers import pipeline

app = FastAPI()
#classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

class InputText(BaseModel):
    text: str

@app.get("/")
def home():
    return {
        "message": "Text Classification API",
        "version": "1.0"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/predict")
def classify_text(data: InputText):
    text = data.text

    prediction = predict(text)

    return {
        "received_text": text,
        "prediction": str(prediction)
        }



