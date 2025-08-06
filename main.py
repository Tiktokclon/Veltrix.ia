from fastapi import FastAPI, Request
from pydantic import BaseModel
import requests

app = FastAPI()

API_URL = "https://api.deepseek.com/v1/chat/completions"
API_KEY = "TON_TOKEN_HUGGINGFACE_ICI"  # Remplace par ton vrai token HuggingFace

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: list[Message]

@app.post("/chat")
def chat(request: ChatRequest):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek-chat",  # ou "deepseek-coder"
        "messages": [msg.dict() for msg in request.messages],
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
