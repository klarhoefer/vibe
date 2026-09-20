# Vibe API

Eine einfache WebAPI mit FastAPI und automatischem Swagger-UI.

## Installation

```bash
uv sync
```

## Starten

```bash
vibe
```

Der Server läuft dann unter `http://localhost:8000`

## Swagger-Dokumentation

Die interaktive Swagger-UI ist verfügbar unter:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API-Endpoints

### Root & Health
- `GET /` - Begrüßungsnachricht
- `GET /health` - Health Check

### Items (CRUD)
- `GET /items` - Alle Artikel abrufen
- `GET /items/{item_id}` - Spezifischen Artikel abrufen
- `POST /items` - Neuen Artikel erstellen
- `PUT /items/{item_id}` - Artikel aktualisieren
- `DELETE /items/{item_id}` - Artikel löschen

## Beispiel-Anfrage

```bash
curl -X POST "http://localhost:8000/items" \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "name": "Beispiel", "description": "Ein Test-Artikel", "price": 99.99}'
```
