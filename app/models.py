from typing import Optional
from pydantic import BaseModel

class WebsiteDetails(BaseModel):
    industry: Optional[str] = None
    company_size: Optional[str] = None
    location: Optional[str] = None
