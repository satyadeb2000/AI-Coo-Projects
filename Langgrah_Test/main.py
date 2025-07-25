from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import os
from fastapi import Request
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/healthcheck")
def healthcheck():
    return JSONResponse(content={"status": "healthy"})

@app.get("/")
def root():
    return RedirectResponse(url="/docs")

class QuestionRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(request: QuestionRequest):
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        return JSONResponse(status_code=500, content={"error": "OpenAI API key not set"})
    try:
        chat = ChatOpenAI(openai_api_key=openai_api_key, model_name="gpt-4-1106-preview")
        answer = chat.predict(request.question)
        return {"answer": answer}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)}) 