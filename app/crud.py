from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app import models, schemas

# Deck CRUD
def get_decks(db: Session):
    return db.query(models.Deck).all()

def create_deck(db: Session, deck: schemas.DeckCreate):
    db_deck = models.Deck(name=deck.name)
    db.add(db_deck)
    db.commit()
    db.refresh(db_deck)
    return db_deck

def delete_deck(db: Session, deck_id: int) -> bool:
    """Delete a deck if it exists, return True if deleted, False otherwise"""
    deck = db.query(models.Deck).filter(models.Deck.id == deck_id).first()
    if deck is None:
        return False
    db.delete(deck)
    db.commit()
    return True

# Flashcard CRUD
def get_flashcards(db: Session, deck_id: int):
    return db.query(models.Flashcard).filter(models.Flashcard.deck_id == deck_id).all()

def create_flashcard(db: Session, flashcard: schemas.FlashcardCreate, deck_id: int):
    """Ensure deck exists before creating a flashcard"""
    deck = db.query(models.Deck).filter(models.Deck.id == deck_id).first()
    if not deck:
        return None  # Deck does not exist

    db_flashcard = models.Flashcard(**flashcard.dict(), deck_id=deck_id)
    db.add(db_flashcard)
    
    try:
        db.commit()
        db.refresh(db_flashcard)
        return db_flashcard
    except IntegrityError:
        db.rollback()
        return None  # Database error (e.g., unique constraint violation)

def delete_flashcard(db: Session, flashcard_id: int) -> bool:
    """Delete a flashcard if it exists, return True if deleted, False otherwise"""
    flashcard = db.query(models.Flashcard).filter(models.Flashcard.id == flashcard_id).first()
    if flashcard is None:
        return False
    db.delete(flashcard)
    db.commit()
    return True
