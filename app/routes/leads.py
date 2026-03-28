from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import SessionLocal

router = APIRouter(prefix="/api/leads", tags=["leads"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.LeadResponse)
def create_lead(lead: schemas.LeadCreate, db: Session = Depends(get_db)):
    db_lead = models.Lead(name=lead.name, phone=lead.phone, message=lead.message)
    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)
    return db_lead

@router.get("/", response_model=list[schemas.LeadResponse])
def read_leads(db: Session = Depends(get_db)):
    leads = db.query(models.Lead).order_by(models.Lead.created_at.desc()).all()
    return leads
