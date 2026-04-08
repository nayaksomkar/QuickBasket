# 🛒 QuickBasket

> WhatsApp-based store ordering system

---

## 🚀 Quick Start

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 3. Install dependencies
pip install psycopg2-binary pymongo reportlab fastapi uvicorn

# 4. Start Docker
docker-compose up -d

# 5. Initialize databases
python initDB.py
# Options: "yes" to drop/recreate, "no" to keep existing

# 6. Run PDF server
python -m uvicorn PDFserver:app --host 0.0.0.0 --port 8001
```

---

## 🐳 Docker Services

| Service   | Port  | Description          |
|-----------|-------|----------------------|
| `mongo`   | 27017 | MongoDB database     |
| `postgres`| 5432  | PostgreSQL database  |
| `n8n`     | 5678  | Workflow automation  |

---

## 🗄️ Database Initialization

### Single Command
```bash
python initDB.py
```
Initializes **both** PostgreSQL and MongoDB databases.

### Separate Commands
```bash
python initPost.py   # PostgreSQL only
python initMongo.py  # MongoDB only
```

Each script asks: `Drop and recreate? (yes/no)`

- **yes** = drops existing and creates fresh
- **no** = creates only if doesn't exist

---

## Database Structure

### PostgreSQL (`quickbasket`)

| Table | Columns |
|-------|---------|
| `products` | name, price |
| `temporary_order` | order_id, order_item, order_quantity, order_price, price_item |

### MongoDB (`quickbasket`)

| Collection | Purpose |
|------------|---------|
| `chat_logs` | Chat messages |
| `order_logs` | Order history |

---

## 📁 Project Files

| File | Description |
|------|-------------|
| `config.py` | All configuration variables |
| `initDB.py` | Initialize PostgreSQL + MongoDB |
| `initPost.py` | Initialize PostgreSQL only |
| `initMongo.py` | Initialize MongoDB only |
| `PDFserver.py` | FastAPI server (PDF generation) |
| `botINS.txt` | Bot instructions |
| `products.csv` | Products list |
| `docker-compose.yml` | Docker services |

---

## 🔌 API Endpoints

### PDF Server (port 8001)
- `POST /generate-pdf` - Generate order PDF

---

## ⌨️ Commands

```bash
# Docker
docker-compose up -d      # Start all services
docker-compose down      # Stop all services

# Database
python initDB.py         # Initialize both
python initPost.py       # PostgreSQL only
python initMongo.py      # MongoDB only

# Server
python -m uvicorn PDFserver:app --port 8001  # Run server
```

---

## 📋 Requirements

- Python 3.11+
- Docker & Docker Compose
- PostgreSQL (via Docker)
- MongoDB (via Docker)
