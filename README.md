# Website Scrapper API

This project provides a **FastAPI** application that allows you to create sessions by scraping content from websites. Once a session is created, you can interact with a **chat API** using the session ID to send and receive messages based on the scraped content.

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
