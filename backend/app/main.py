from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import models as models
from models import Base, Category
from databaseconfig import SessionLocal,engine
from sqlalchemy.orm import Session
from schemas import CategoryBase

app = FastAPI()

# Enable CORS so your React app can talk to the backend safely
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # Default Vite React port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
def health_check():
    return {"status": "FinLog backend is running!"}

def init_db():
    models.Base.metadata.create_all(bind=engine) # will create the tables in the database based on the models defined in models.py

init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/categories")
def create_category(category: CategoryBase, db: Session = Depends(get_db)):
    db.add(models.Category(**category.model_dump()))
    db.commit()
    db.refresh(category)
    return category