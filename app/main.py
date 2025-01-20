from fastapi import FastAPI, Depends, HTTPException

from app.openai_api import get_answers_from_openai
from .models import WebsiteDetails
from .scrapper import scrape_website
from .security import validate_secret_key
import logging
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

@app.post("/scrape-website", response_model=WebsiteDetails)
async def scrape_website_endpoint(
    url: str,
    authorization: str = Depends(validate_secret_key)
) -> WebsiteDetails:
    try:
        website_details = scrape_website(url)
        
        answers = get_answers_from_openai(website_details)
        
        return WebsiteDetails(
            industry=answers["industry"],
            company_size=answers["company_size"],
            location=answers["location"]
        )
    except Exception as e:
        logging.error(f"Error scraping website: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Error scraping the website: {str(e)}")
