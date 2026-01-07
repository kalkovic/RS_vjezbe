# Category Service

Category Service je mikroservis zadužen za upravljanje kategorijama vijesti.
Izlaže REST API koji koriste news-service i frontend aplikacija.

## Pokretanje servisa

```bash
cd my_app/checkpoint_2/category_service
pip install -r requirements.txt
uvicorn category_service.app:app --reload --port 8002
```