# FastAPI AI Agent for Website Scraping and OpenAI Integration

## Overview

This project implements a FastAPI application that uses an AI agent to scrape a website's homepage and answer three specific questions based on the content:

- **Industry**: What industry does the website belong to?
- **Company Size**: What is the size of the company (e.g., small, medium, large)?
- **Location**: Where is the company located?

The AI agent processes the raw text of the homepage using OpenAI's API to answer these questions.

## Prerequisites

Before running the project, ensure that you have:

- **Python 3.11** or higher installed
- The dependencies listed in `requirements.txt`

---

## Steps to Get Started

1. **Clone the repository**

   To begin, clone this repository to your local machine by running:

   ```bash
   git clone https://github.com/sumitabh1710/website_scrapper
   cd website-scrapper


2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

3. **Run the application**
   ```bash
   uvicorn app.main:app --reload

( Please change the API key in .env file )

Once the application is running, you can access the Swagger documentation for the API by navigating to:

http://127.0.0.1:8000/docs

The Swagger UI will allow you to test and interact with the available API endpoints.

Thank You
