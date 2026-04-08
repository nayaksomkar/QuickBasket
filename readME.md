# 🛒 QuickBasket

> WhatsApp store ordering system with n8n automation, PostgreSQL, MongoDB, and PDF generation

---

## 📸 Preview

### Chat View 1

![WhatsApp Chat 2](https://raw.githubusercontent.com/nayaksomkar/QuickBasket/main/images/whatsapp_chat_image_2.png)

### Chat View 2

![WhatsApp Chat 1](https://raw.githubusercontent.com/nayaksomkar/QuickBasket/main/images/whatsapp_chat_image_1.png)

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

```
WhatsApp Trigger → AI Agent (LangChain) → Simple Memory → WhatsApp Send
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

# 5. Start Docker
docker-compose up -d

# 6. Initialize databases
python initDB.py

# 7. Import n8n workflow
# Open http://localhost:5678
# Import: workflows/QuickBasket.n8n.json

# 8. Run PDF server
python -m uvicorn PDFserver:app --port 8001
```

---

## 🗄️ Database

### PostgreSQL (`quickbasket`)
- `products` (name, price)
- `temporary_order` (order details)

### MongoDB (`quickbasket`)
- `chat_logs`
- `order_logs`

---

## 📁 Project Structure

```
QuickBasket/
├── config.py              # Configuration
├── initDB.py              # Initialize databases
├── initPost.py            # PostgreSQL setup
├── initMongo.py           # MongoDB setup
├── PDFserver.py           # PDF server
├── botINS.txt             # Bot instructions
├── products.csv          # Products list
├── requirements.txt       # Dependencies
├── docker-compose.yml    # Docker services
├── .env.example          # Env template
├── workflows/             # n8n workflow
├── images/               # Images
├── OrderPDF/             # Generated PDFs
└── mongo/                # MongoDB data
```

---

## 🔌 API

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/generate-pdf` | POST | Generate PDF |

---

## ⚡ Tech Stack

- **Backend**: FastAPI, uvicorn
- **Database**: PostgreSQL, MongoDB
- **Automation**: n8n (LangChain AI)
- **PDF**: ReportLab

---

## 🔧 Config

```env
POSTGRES_PASSWORD=your_password
WEBHOOK_URL=https://your-ngrok-url.ngrok-free.dev
```
