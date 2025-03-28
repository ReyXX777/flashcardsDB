from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Load environment variables (only needed for local development)
load_dotenv()

print(f"DATABASE_URL: {os.getenv('DATABASE_URL')}")  # <-- Add this line


# Ensure DATABASE_URL is set
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("🚨 DATABASE_URL is not set! Make sure to define it in your Railway environment settings.")

# Create database engine
engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20)

# Session configuration
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
