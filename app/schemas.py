from pydantic import BaseModel
from datetime import datetime

class LeadCreate(BaseModel):
    name: str
    phone: str
    message: str | None = None

class LeadResponse(BaseModel):
    id: int
    name: str
    phone: str
    message: str | None = None
    created_at: datetime

    class Config:
        from_attributes = True
