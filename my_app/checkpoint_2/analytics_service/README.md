# Analytics Service

Analytics Service je mikroservis zadužen za analizu i statistiku vijesti
(npr. broj vijesti po kategoriji).

## Pokretanje servisa

```bash
cd my_app/checkpoint_2/analytics-service
pip install -r requirements.txt
uvicorn analytics-service.app:app --reload --port 8003
```