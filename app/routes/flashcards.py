from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud, schemas

router = APIRouter(prefix="/flashcards", tags=["Flashcards"])

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{deck_id}", response_model=list[schemas.FlashcardResponse])
def read_flashcards(deck_id: int, db: Session = Depends(get_db)):
    """Fetch all flashcards in a deck"""
    flashcards = crud.get_flashcards(db, deck_id)
    if flashcards is None:
        raise HTTPException(status_code=404, detail="Deck not found")
    return flashcards

@router.post("/{deck_id}", response_model=schemas.FlashcardResponse)
def create_flashcard(deck_id: int, flashcard: schemas.FlashcardCreate, db: Session = Depends(get_db)):
    """Create a new flashcard in a deck"""
    new_flashcard = crud.create_flashcard(db, flashcard, deck_id)
    if new_flashcard is None:
        raise HTTPException(status_code=400, detail="Deck not found or invalid flashcard data")
    return new_flashcard

@router.delete("/{flashcard_id}")
def delete_flashcard(flashcard_id: int, db: Session = Depends(get_db)):
    """Delete a flashcard by ID"""
    deleted = crud.delete_flashcard(db, flashcard_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Flashcard not found")
    return {"message": "Flashcard deleted successfully"}
