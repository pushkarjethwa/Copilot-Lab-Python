"""
Unit tests for the main API endpoints.
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root_endpoint():
    """Test the root endpoint returns welcome message."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Copilot Lab Python API"}


def test_get_items_empty():
    """Test getting items when list is empty."""
    response = client.get("/items")
    assert response.status_code == 200
    assert "items" in response.json()


def test_create_item():
    """Test creating a new item."""
    item_data = {
        "name": "Test Item",
        "description": "A test item",
        "price": 10.99,
        "in_stock": True
    }
    response = client.post("/items", json=item_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Test Item"
    assert response.json()["price"] == 10.99


def test_get_item_by_id():
    """Test getting a specific item by ID."""
    # First create an item
    item_data = {
        "name": "Test Item",
        "description": "A test item",
        "price": 10.99,
        "in_stock": True
    }
    create_response = client.post("/items", json=item_data)
    item_id = create_response.json()["id"]
    
    # Then retrieve it
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Item"


def test_get_nonexistent_item():
    """Test getting an item that doesn't exist."""
    response = client.get("/items/9999")
    assert response.status_code == 200
    assert "error" in response.json()
