from fastapi import FastAPI
from app.routes import decks, flashcards
from app.database import engine, Base

app = FastAPI(title="Flashcard API", version="1.0")

# Ensure database tables are created (if they don't exist)
Base.metadata.create_all(bind=engine)

# Include API routes
app.include_router(decks.router)
app.include_router(flashcards.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Flashcard API"}
