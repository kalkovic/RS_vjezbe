# Analytics Service

Analytics Service je mikroservis zadužen za analizu i statistiku vijesti
(npr. broj vijesti po kategoriji).

## Pokretanje servisa

```bash
cd analytics-service
pip install -r requirements.txt
uvicorn app:app --reload --port 8003
```