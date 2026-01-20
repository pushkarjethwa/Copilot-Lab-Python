"""
Main FastAPI application entry point.
"""
from fastapi import FastAPI, HTTPException
from app.models import Item
from app.services import ItemService

app = FastAPI(title="Copilot Lab Python API")
item_service = ItemService()


@app.get("/")
async def root():
    """Root endpoint returning a welcome message."""
    return {"message": "Welcome to Copilot Lab Python API"}


@app.get("/items")
async def get_items():
    """Get all items."""
    return {"items": item_service.get_all_items()}


@app.get("/items/{item_id}")
async def get_item(item_id: int):
    """Get a specific item by ID."""
    item = item_service.get_item_by_id(item_id)
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items")
async def create_item(item: Item):
    """Create a new item."""
    return item_service.create_item(item)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
