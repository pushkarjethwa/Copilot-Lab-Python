"""
Data models for the API.
"""
from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    """Item model representing a basic data entity."""
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True
