# News Service

News Service je mikroservis zadužen za dohvat i obradu vijesti.
Izlaže REST API koji koriste frontend i ostali servisi.

## Pokretanje servisa

```bash
cd my_app/checkpoint_2/news_service
pip install -r requirements.txt
uvicorn news_service.app:app --reload --port 8001
```