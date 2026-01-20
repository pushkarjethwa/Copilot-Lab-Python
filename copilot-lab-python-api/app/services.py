"""
Business logic services for the API.
"""
from typing import List, Optional
from app.models import Item


class ItemService:
    """Service class for managing items."""
    
    def __init__(self):
        """Initialize the service with an empty items list."""
        self.items: List[Item] = []
        self.next_id = 1
    
    def get_all_items(self) -> List[Item]:
        """Retrieve all items."""
        return self.items
    
    def get_item_by_id(self, item_id: int) -> Optional[Item]:
        """Retrieve a specific item by its ID."""
        for item in self.items:
            if item.id == item_id:
                return item
        return None
    
    def create_item(self, item: Item) -> Item:
        """Create a new item and add it to the list."""
        item.id = self.next_id
        self.next_id += 1
        self.items.append(item)
        return item
