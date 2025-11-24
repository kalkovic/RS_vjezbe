# News Aggregator (Checkpoint 1)

Jednostavna Python aplikacija za prikaz vijesti napravljena kao dio projektnog zadatka.  
Aplikacija koristi Tkinter za GUI i čita vijesti iz lokalnog JSON-a (`newsapp/data/news.json`).

Projekt je razvijen tako da bude jednostavan, monolitan i prikladan za Checkpoint 1.  
---

## Tehnologije

- **Python 3.10+**
- **Tkinter** (ugrađen u Python)
- **JSON za spremanje vijesti**
- **Conda virtualno okruženje**
- (Opcionalno kasnije: FastAPI, Docker, DynamoDB, blockchain modul)

---

## Struktura projekta
my_app/
    newsapp/
        core/
            domain.py
            services.py
        ui/
            gui.py
main.py
README.md
requirements.txt


### 1. Kreiranje conda okruženja

```bash
conda create -n newsapp python=3.10
conda activate newsapp

pip install -r requirements.txt
python main.py
