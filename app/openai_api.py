import openai
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

def get_answers_from_openai(scraped_text: str) -> dict:
    prompt = f"""
    Using the following homepage content, please answer these questions:
    1. Industry: What industry does the website belong to?
    2. Company Size: What is the size of the company (e.g., small, medium, large) if mentioned?
    3. Location: Where is the company located (if mentioned)?

    Homepage content:
    {scraped_text}
    """
    
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=500,
        temperature=0.7,
    )

    response_text = response.choices[0].text.strip()
    
    print(response_text)

    return parse_openai_response(response_text)

def parse_openai_response(response_text: str) -> dict:
    lines = response_text.split("\n")
    answers = {
        "industry": "",
        "company_size": "",
        "location": ""
    }

    for line in lines:
        if line.lower().startswith("industry:"):
            answers["industry"] = line[len("Industry:"):].strip()
        elif line.lower().startswith("company size:"):
            answers["company_size"] = line[len("Company Size:"):].strip()
        elif line.lower().startswith("location:"):
            answers["location"] = line[len("Location:"):].strip()

    return answers
