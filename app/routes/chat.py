from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv
from app.auth import verify_auth
from .session import load_sessions

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

router = APIRouter()

class ChatRequest(BaseModel):
    question: str

@router.post("/chat/{session_id}")
async def chat_with_ai(session_id: str, request: ChatRequest, auth: str = Depends(verify_auth)):
    scraped_data = get_scraped_data(session_id)
    if not scraped_data:
        raise HTTPException(status_code=404, detail="Session not found")

    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=f"Answer the following question based on the scraped content: {scraped_data}\nQuestion: {request.question}",
            max_tokens=100,
            temperature=0.7,
        )
        answer = response.choices[0].text.strip()
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_scraped_data(session_id: str):
    sessions = load_sessions()
    return sessions.get(session_id)
