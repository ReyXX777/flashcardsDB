from pydantic import BaseModel
from typing import List, Optional

class FlashcardBase(BaseModel):
    question: str
    answer: str
    ease_factor: Optional[float] = 2.5  # Changed to float
    due: Optional[bool] = False

class FlashcardCreate(FlashcardBase):
    pass

class FlashcardResponse(FlashcardBase):
    id: int
    deck_id: int
    due: bool = False  # Ensures due is always returned

    class Config:
        from_attributes = True  # Updated for Pydantic v2 compatibility

class DeckBase(BaseModel):
    name: str

class DeckCreate(DeckBase):
    pass

class DeckResponse(DeckBase):
    id: int
    flashcards: Optional[List[FlashcardResponse]] = []  # Ensures an empty list if no flashcards exist

    class Config:
        from_attributes = True  # Updated for Pydantic v2 compatibility
