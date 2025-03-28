from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud, schemas

router = APIRouter(prefix="/decks", tags=["Decks"])

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.DeckResponse])
def read_decks(db: Session = Depends(get_db)):
    """Fetch all decks"""
    return crud.get_decks(db)

@router.post("/", response_model=schemas.DeckResponse)
def create_deck(deck: schemas.DeckCreate, db: Session = Depends(get_db)):
    """Create a new deck"""
    return crud.create_deck(db, deck)

@router.delete("/{deck_id}")
def delete_deck(deck_id: int, db: Session = Depends(get_db)):
    """Delete a deck by ID"""
    deleted = crud.delete_deck(db, deck_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Deck not found")
    return {"message": "Deck deleted successfully"}
