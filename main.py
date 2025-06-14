from fastapi import FastAPI, Request
from pydantic import BaseModel
import openai

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/api/")
async def answer_question(request: Request, question_request: QuestionRequest):
    return {"answer": f"You asked: {question_request.question}"}
