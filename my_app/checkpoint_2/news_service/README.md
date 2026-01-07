# News Service

News Service je mikroservis zadužen za dohvat i obradu vijesti.
Izlaže REST API koji koriste frontend i ostali servisi.

## Pokretanje servisa

```bash
cd cd my_app/checkpoint_2/news-service
pip install -r requirements.txt
uvicorn news-service.app:app --reload --port 8001
```