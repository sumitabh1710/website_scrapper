from fastapi import FastAPI
from app.routes import session, chat
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="FastAPI Scraper with AI Agent",
    description="Scrape websites and answer questions using an AI agent",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

app.include_router(session.router, prefix="/api", tags=["Session"])
app.include_router(chat.router, prefix="/api", tags=["Chat"])
