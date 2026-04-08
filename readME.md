# 🛒 QuickBasket

WhatsApp store ordering system with n8n automation, PostgreSQL, MongoDB, and PDF generation

---

## What is QuickBasket?

QuickBasket is a WhatsApp-based ordering system where customers can browse products, add items to cart, and place orders - all through WhatsApp chat.

---

## Preview

<table align="center">
<tr>
<td align="center"><img src="https://github.com/nayaksomkar/QuickBasket/raw/main/images/whatsapp_chat_image_2.png" width="350"/></td>
<td align="center"><img src="https://github.com/nayaksomkar/QuickBasket/raw/main/images/whatsapp_chat_image_1.png" width="350"/></td>
</tr>
</table>

---

## Architecture

```
User → WhatsApp → n8n → AI Agent → Database → PDF
```

---

## n8n Workflow

```
WhatsApp Trigger → AI Agent → Memory → WhatsApp Reply
```

### Intent Flow

```
User Message → Parse Intent
     |
     ▼
add/remove/confirm/noaction
```

---

## Docker Services

| Service | Port | Purpose |
|---------|------|---------|
| mongo | 27017 | NoSQL database |
| postgres | 5432 | SQL database |
| n8n | 5678 | Automation |

---

## Database

### PostgreSQL
- products (name, price)
- temporary_order (order details)

### MongoDB
- chat_logs
- order_logs

---

## Quick Start

```bash
# Setup
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# Config
copy .env.example .env

# Run
docker-compose up -d
python initDB.py
python -m uvicorn PDFserver:app --port 8001
```

---

## Project Files

```
config.py      - Configuration
initDB.py     - Initialize databases
initPost.py   - PostgreSQL setup
initMongo.py  - MongoDB setup
PDFserver.py  - PDF generation
botINS.txt    - Bot instructions
products.csv  - Products list
requirements.txt
docker-compose.yml
workflows/    - n8n workflows
images/       - Preview images
OrderPDF/     - Generated PDFs
```

---

## API

POST /generate-pdf - Generate order PDF

---

## Tech Stack

FastAPI, uvicorn, PostgreSQL, MongoDB, n8n (LangChain AI), ReportLab, Docker

---

## Bot Intents

| Intent | Action |
|--------|--------|
| add | Add to cart |
| remove | Remove from cart |
| confirm | Confirm order |
| noaction | No action needed |

---

## Products

20 products: snacks & ice creams. See products.csv

---

## Config

Create .env:
```
POSTGRES_PASSWORD=your_password
WEBHOOK_URL=https://your-ngrok-url.ngrok-free.dev
```
