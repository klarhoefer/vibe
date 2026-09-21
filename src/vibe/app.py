from fastapi import FastAPI, HTTPException

from .models import Item, Message

app = FastAPI(
    title="Vibe API",
    description="Eine einfache WebAPI mit FastAPI und Swagger",
    version="0.1.0",
)


# In-Memory Datenbank für Demo-Zwecke
items_db: dict[int, Item] = {}


@app.get("/", tags=["Root"])
def read_root() -> Message:
    """Root-Endpoint der API."""
    return Message(message="Willkommen bei der Vibe API!")


@app.get("/health", tags=["Health"])
def health_check() -> dict[str, str]:
    """Health Check Endpoint."""
    return {"status": "healthy"}


@app.get("/items", tags=["Items"])
def list_items() -> list[Item]:
    """Liste alle Artikel auf."""
    return list(items_db.values())


@app.get("/items/{item_id}", tags=["Items"])
def get_item(item_id: int) -> Item:
    """Abrufen eines spezifischen Artikels."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Artikel nicht gefunden")
    return items_db[item_id]


@app.post("/items", tags=["Items"])
def create_item(item: Item) -> Item:
    """Einen neuen Artikel erstellen."""
    if item.id in items_db:
        raise HTTPException(status_code=400, detail="Artikel mit dieser ID existiert bereits")
    items_db[item.id] = item
    return item


@app.put("/items/{item_id}", tags=["Items"])
def update_item(item_id: int, item: Item) -> Item:
    """Einen Artikel aktualisieren."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Artikel nicht gefunden")
    items_db[item_id] = item
    return item


@app.delete("/items/{item_id}", tags=["Items"])
def delete_item(item_id: int) -> Message:
    """Einen Artikel löschen."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Artikel nicht gefunden")
    del items_db[item_id]
    return Message(message=f"Artikel {item_id} wurde gelöscht")
