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

@app.post("/api/category")
def create_category(category: CategoryBase, db: Session = Depends(get_db)):
    db_category = models.Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

@app.get("/api/category")
def read_categories(db: Session = Depends(get_db)):
    categories = db.query(models.Category).all()
    return categories

@app.delete("/api/category/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if category:
        db.delete(category)
        db.commit()
        return {"message": "Category deleted successfully"}
    else:
        return {"message": "Category not found"}
    
# @app.put("/api/category/{category_id}")
# def update_category(category_id: int, category: CategoryBase, db: Session = Depends(get_db)):
#     db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
#     if db_category:
#         db_category.name = category.name
#         db.commit()
#         db.refresh(db_category)
#         return db_category
#     else:
#         return {"message": "Category not found"}
    
