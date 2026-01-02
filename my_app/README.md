# News Aggregator (Checkpoint 1)

Jednostavna Python aplikacija za prikaz vijesti napravljena kao dio projektnog zadatka.  
Aplikacija koristi Tkinter za GUI i čita vijesti iz lokalnog JSON-a (`newsapp/data/news.json`).

Projekt je razvijen tako da bude jednostavan, monolitan i prikladan za Checkpoint 1.  
---

# News Aggregator (Checkpoint 2)

Aplikacija je podijeljena na više neovisnih mikroservisa koji međusobno
komuniciraju putem REST API-ja.

Service-to-service komunikacija

Komunikacija se ostvaruje sinkrono putem REST API-ja (HTTP).
analytics-service šalje HTTP GET zahtjeve prema ostalim servisima.
Odabrana je REST komunikacija jer je jednostavna, čitljiva i dovoljna
za lokalnu razvojnu razinu aplikacije.
---

## Tehnologije

- **Python 3.10+**
- **Tkinter** (ugrađen u Python)
- **JSON za spremanje vijesti**
- **Conda virtualno okruženje**
---

## Struktura projekta
```my_app/
│
├─ checkpoint-1/                      ← PRVI CHECKPOINT (monolit + GUI)
│  │
│  ├─ build/                          ← PyInstaller artefakti
│  ├─ dist/
│  │  └─ main.exe                     ← standalone aplikacija (opcionalno)
│  │
│  ├─ newsapp/
│  │  ├─ core/
│  │  │  ├─ __init__.py
│  │  │  ├─ domain.py                 ← NewsItem model
│  │  │  └─ services.py               ← poslovna logika
│  │  │
│  │  ├─ data/
│  │  │  ├─ __init__.py
│  │  │  ├─ news.json                 ← lokalni podaci
│  │  │  └─ storage.py                ← čitanje JSON-a
│  │  │
│  │  ├─ ui/
│  │  │  ├─ __init__.py
│  │  │  └─ gui.py                    ← Tkinter GUI
│  │  │
│  │  ├─ utils/
│  │  │  ├─ __init__.py
│  │  │  └─ helpers.py                ← pomoćne funkcije
│  │  │
│  │  └─ config.py                    ← putanje / konfiguracija
│  │
│  ├─ main.py                         ← ulazna točka aplikacije
│  ├─ main.spec                       ← PyInstaller konfiguracija
│  ├─ requirements.txt
│  └─ README.md
│
├─ checkpoint-2/                      ← DRUGI CHECKPOINT (mikroservisi)
│  │
│  ├─ news-service/
│  │  ├─ app.py                       ← FastAPI servis za vijesti
│  │  ├─ db.py                        ← SQLite inicijalizacija
│  │  ├─ models.py                    ← modeli podataka
│  │  ├─ requirements.txt
│  │  ├─ .env.example
│  │  └─ README.md
│  │
│  ├─ category-service/
│  │  ├─ app.py                       ← servis za kategorije
│  │  ├─ db.py
│  │  ├─ models.py
│  │  ├─ requirements.txt
│  │  ├─ .env.example
│  │  └─ README.md
│  │
│  ├─ analytics-service/              ← (kod tebe: analytics-service)
│  │  ├─ app.py                       ← agregacija podataka
│  │  ├─ services.py                  ← pozivi prema drugim servisima
│  │  ├─ requirements.txt
│  │  ├─ .env.example
│  │  └─ README.md
│  │
│  └─ README.md                       ← glavni README za CP2
│
└─ README.md                          ← (opcionalno) opis cijelog projekta

### 1. Kreiranje conda okruženja

```bash
conda create -n newsapp python=3.10
conda activate newsapp

pip install -r requirements.txt
python main.py

### 1. Kreiranje jedinstveni paket aplikacije pomoću alata PyInstaller-a

pip install pyinstaller

pyinstaller --noconsole --onefile main.py

### 2. API dokumentacija
Svaki mikroservis koristi FastAPI te automatski generira Swagger dokumentaciju:

News Service: http://localhost:8001/docs

Category Service: http://localhost:8002/docs

Analytics Service: http://localhost:8003/docs