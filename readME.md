# 🛒 QuickBasket

> WhatsApp store ordering system with n8n automation, PostgreSQL, MongoDB, and PDF generation

---

## 🏗️ Architecture

```
User → WhatsApp → n8n (AI Agent) → PostgreSQL/MongoDB
                     ↓
               PDF Generation
```

---

## 🐳 Docker Services

| Service   | Port  | Description          |
|-----------|-------|----------------------|
| `mongo`   | 27017 | MongoDB database     |
| `postgres`| 5432  | PostgreSQL database  |
| `n8n`     | 5678  | Workflow automation  |

---

## ⚙️ n8n Workflow

The n8n workflow handles all WhatsApp messages:

```
┌─────────────────────┐
│  WhatsApp Trigger   │  ← Receives message from user
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│     AI Agent        │  ← Processes with bot instructions
│   (LangChain)       │    - add, remove, confirm, noaction
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│   Simple Memory     │  ← Keeps conversation history
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│   WhatsApp Node     │  ← Sends reply to user
└─────────────────────┘
```

### Intent Types
| Intent    | Action                          |
|-----------|--------------------------------|
| `add`     | Add items to order              |
| `remove`  | Remove items from order         |
| `confirm` | Confirm and place order         |
| `noaction`| No action needed                |

---

## 🚀 Quick Start

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Copy environment file
copy .env.example .env
# Edit .env with your values

# 5. Start Docker
docker-compose up -d

# 6. Initialize databases
python initDB.py

# 7. Start n8n
docker-compose up -d n8n

# 8. Import workflow
# Open n8n at http://localhost:5678
# Import workflows/QuickBasket.n8n.json

# 9. Run PDF server
python -m uvicorn PDFserver:app --port 8001
```

---

## 🗄️ Database Initialization

```bash
python initDB.py         # Both PostgreSQL + MongoDB
python initPost.py       # PostgreSQL only
python initMongo.py      # MongoDB only
```

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

```
QuickBasket/
├── config.py              # Configuration (loads from .env)
├── initDB.py              # Initialize both databases
├── initPost.py           # Initialize PostgreSQL
├── initMongo.py          # Initialize MongoDB
├── PDFserver.py           # PDF generation server
├── botINS.txt            # Bot instructions for AI
├── products.csv          # Products list
├── requirements.txt      # Python dependencies
├── docker-compose.yml    # Docker services
├── .env.example          # Environment template
├── .env                  # Your environment variables
├── workflows/
│   └── QuickBasket.n8n.json  # n8n workflow
├── OrderPDF/             # Generated PDFs
└── README.md
```

---

## 🔌 API Endpoints

### PDF Server (port 8001)
- `POST /generate-pdf` - Generate order PDF

---

## 📋 Requirements

- Python 3.11+
- Docker & Docker Compose
- PostgreSQL, MongoDB, n8n (via Docker)

---

## 🔧 Configuration

Edit `.env` file:
```env
POSTGRES_PASSWORD=your_password
WEBHOOK_URL=https://your-ngrok-url.ngrok-free.dev
```
