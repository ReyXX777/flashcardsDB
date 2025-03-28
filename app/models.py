from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship
from app.database import Base

class Deck(Base):
    __tablename__ = "decks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    
    # Cascade delete ensures all related flashcards are deleted when a deck is deleted
    flashcards = relationship("Flashcard", back_populates="deck", cascade="all, delete")

class Flashcard(Base):
    __tablename__ = "flashcards"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, index=True, nullable=False)
    answer = Column(String, nullable=False)
    ease_factor = Column(Float, default=2.5)  # Changed to Float for better accuracy
    due = Column(Boolean, server_default="false")  # Ensures PostgreSQL compatibility
    deck_id = Column(Integer, ForeignKey("decks.id", ondelete="CASCADE"), nullable=False)

    deck = relationship("Deck", back_populates="flashcards")
