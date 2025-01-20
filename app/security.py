from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from dotenv import load_dotenv
import os

load_dotenv()

bearer_scheme = HTTPBearer()

SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")

def validate_secret_key(credentials: HTTPAuthorizationCredentials = Security(bearer_scheme)) -> str:
    if credentials.credentials != SECRET_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")
    return "user1"
