# Category Service

Category Service je mikroservis zadužen za upravljanje kategorijama vijesti.
Izlaže REST API koji koriste news-service i frontend aplikacija.

## Pokretanje servisa

```bash
cd category-service
pip install -r requirements.txt
uvicorn app:app --reload --port 8002
```