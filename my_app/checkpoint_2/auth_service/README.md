# Authentication service
Auth Service je zaseban mikroservis zadužen za 
autentifikaciju korisnika u sustavu agregatora vijesti.

## Pokretanje servisa

```bash
cd my_app/checkpoint_2
pip install -r requirements.txt
uvicorn auth_service.app:app --reload --port 8000
```