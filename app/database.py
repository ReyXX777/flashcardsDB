from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Print DATABASE_URL for debugging
print(f"DATABASE_URL: {os.getenv('DATABASE_URL')}")  # <-- This will print the DATABASE_URL

# Print all environment variables for debugging
print("All environment variables:")
for key, value in os.environ.items():
    print(f"{key}: {value}")

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
