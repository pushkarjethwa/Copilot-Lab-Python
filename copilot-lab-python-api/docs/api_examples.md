# API Examples

This document provides examples of how to use the Copilot Lab Python API.

## Base URL

```
http://localhost:8000
```

## Endpoints

### Get Welcome Message

```bash
curl http://localhost:8000/
```

Response:
```json
{
  "message": "Welcome to Copilot Lab Python API"
}
```

### Get All Items

```bash
curl http://localhost:8000/items
```

Response:
```json
{
  "items": []
}
```

### Create an Item

```bash
curl -X POST http://localhost:8000/items \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Sample Item",
    "description": "This is a sample item",
    "price": 29.99,
    "in_stock": true
  }'
```

Response:
```json
{
  "id": 1,
  "name": "Sample Item",
  "description": "This is a sample item",
  "price": 29.99,
  "in_stock": true
}
```

### Get Item by ID

```bash
curl http://localhost:8000/items/1
```

Response:
```json
{
  "id": 1,
  "name": "Sample Item",
  "description": "This is a sample item",
  "price": 29.99,
  "in_stock": true
}
```

## Testing with Python

```python
import httpx

# Get welcome message
response = httpx.get("http://localhost:8000/")
print(response.json())

# Create an item
item_data = {
    "name": "Python Item",
    "description": "Created with Python",
    "price": 19.99,
    "in_stock": True
}
response = httpx.post("http://localhost:8000/items", json=item_data)
print(response.json())

# Get all items
response = httpx.get("http://localhost:8000/items")
print(response.json())
```
