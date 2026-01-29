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

# News Aggregator (Checkpoint 2)
U sklopu Checkpointa 3, postojeća mikroservisna arhitektura proširena je
korištenjem Docker tehnologije s ciljem pojednostavljenja lokalnog
pokretanja i upravljanja servisima.

Svaki mikroservis je zapakiran u vlastiti Docker image, dok se
cjelokupna aplikacija pokreće pomoću Docker Compose alata.
Na taj način osigurano je konzistentno okruženje za izvođenje aplikacije
bez potrebe za ručnim podešavanjem virtualnih okruženja.

Komunikacija između mikroservisa i dalje se odvija sinkrono putem
REST API-ja (HTTP), dok Docker mreža omogućuje pouzdanu međusobnu
povezanost servisa unutar istog okruženja.
---
## Tehnologije

- **Python 3.10+**
- **Tkinter** (ugrađen u Python)
- **JSON za spremanje vijesti**
- **Conda virtualno okruženje**
---

### 1. Kreiranje jedinstveni paket aplikacije pomoću alata PyInstaller-a

pip install pyinstaller

pyinstaller --noconsole --onefile main.py


### 1. Kreiranje conda okruženja

```bash
conda create -n newsapp python=3.10
conda activate newsapp

pip install -r requirements.txt
python main.py
```

### 2. API dokumentacija
Svaki mikroservis koristi FastAPI te automatski generira Swagger dokumentaciju:

News Service: http://localhost:8001/docs

Authentication Service: http://localhost:8002/docs

Analytics Service: http://localhost:8003/docs

## Struktura projekta
```my_app/
├─ checkpoint-1/
│  ├─ build/
│  ├─ dist/
│  │  └─ main.exe
│  │
│  ├─ newsapp/
│  │  ├─ core/
│  │  ├─ data/
│  │  ├─ ui/
│  │  ├─ utils/
│  │  └─ config.py
│
├─ checkpoint-2/
│  │
│  ├─ news_service/
│  │  ├─ app.py              
│  │  ├─ db.py               
│  │  ├─ models.py           
│  │  ├─ requirements.txt
│  │  ├─ .env.example
│  │  ├─ __init__.py
│  │  └─ README.md
│  │
│  ├─ auth_service/
│  │  ├─ app.py              
│  │  ├─ db.py               
│  │  ├─ requirements.txt
│  │  ├─ .env.example
│  │  ├─ __init__.py
│  │  └─ README.md
│  │
│  ├─ analytics_service/
│  │  ├─ app.py             
│  │  ├─ services.py         
│  │  ├─ requirements.txt
│  │  ├─ .env.example
│  │  ├─ __init__.py
│  │  └─ README.md
│  │
│  ├─ frontend/
│  │  ├─ index.html          
│  │  └─ app.js              
│  │
│  ├─ docker-compose.yml     
│  ├─ users.db               
│  └─ RS_2_kalkovic.drawio.png  
│
│checkpoint-3/                      
│  │
│  ├─ news-service/
│  │  ├─ app.py                       
│  │  ├─ db.py                        
│  │  ├─ models.py                   
│  │  ├─ requirements.txt
│  │  ├─ .env.example
│  │  ├─ __init__.py
│  │  ├─ Dockerfile
│  │  └─ README.md
│  │
│  ├─ auth-service/
│  │  ├─ app.py                       
│  │  ├─ db.py
│  │  ├─ requirements.txt
│  │  ├─ .env.example
│  │  ├─ __init__.py
│  │  ├─ Dockerfile
│  │  └─ README.md
│  │
│  └─ analytics-service/              
│     ├─ app.py                       
│     ├─ services.py                  
│     ├─ requirements.txt
│     ├─ .env.example
│     ├─ __init__.py
│     ├─ Dockerfile
│     └─ README.md  
├─ main.py
├─ main.spec
├─ requirements.txt
└─ README.md
```                 