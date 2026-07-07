import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#DATABASE_URL = "postgresql://postgres:test123@localhost:5432/finlog"

DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://postgres:test123@localhost:5432/finlog"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)