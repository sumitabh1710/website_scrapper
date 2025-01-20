import json
import os
import uuid
from fastapi import APIRouter, HTTPException, Depends
from app.services.scraper import scrape_website
from app.auth import verify_auth

router = APIRouter()

@router.post("/session")
async def create_session(url: str, auth: str = Depends(verify_auth)):
    scraped_content = scrape_website(url)
    if not scraped_content:
        raise HTTPException(status_code=404, detail="Could not scrape website content")

    session_id = str(uuid.uuid4())
    save_scraped_data(session_id, scraped_content)

    return {"session_id": session_id, "scraped_content": scraped_content}

@router.get("/sessions")
async def get_sessions(auth: str = Depends(verify_auth)):
    sessions = load_sessions()
    if not sessions:
        raise HTTPException(status_code=404, detail="No sessions found")

    return {"sessions": sessions}

def save_scraped_data(session_id, scraped_content):
    file_path = 'session.json'

    sessions = load_sessions()

    if session_id not in sessions:
        sessions[session_id] = {'scraped_content': scraped_content}

    with open(file_path, 'w') as f:
        json.dump(sessions, f, indent=4)

def load_sessions():
    file_path = 'session.json'

    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        return {}

    with open(file_path, 'r') as f:
        return json.load(f)
