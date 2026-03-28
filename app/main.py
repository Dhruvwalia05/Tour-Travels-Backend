from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routes import leads

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Ganpati Tour & Travels API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173","https://ganpatitoursandtravel.onrender.com",],  # Vite default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(leads.router)

@app.get("/")
def root():
    return {"message": "Ganpati Tour & Travels API"}
