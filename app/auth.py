from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from dotenv import load_dotenv
import os

bearer_scheme = HTTPBearer()

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

def verify_auth(credentials: HTTPAuthorizationCredentials = Security(bearer_scheme)):
    if credentials.credentials != SECRET_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")
    return "user1"
