# =============================================================================
# Configuration File
# Contains all database and server configuration variables
# Sensitive values loaded from environment variables
# =============================================================================

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# =============================================================================
# PostgreSQL Configuration
# =============================================================================

POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", "5432"))
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "pass")
POSTGRES_DB_DEFAULT = "postgres"

# PostgreSQL Database Names
POSTGRES_DB_QUICKBASKET = "quickbasket"

# PostgreSQL Table Names
POSTGRES_TABLE_PRODUCTS = "products"
POSTGRES_TABLE_TEMP_ORDER = "temporary_order"
POSTGRES_TABLE_ORDERS = "orders"
POSTGRES_TABLE_ORDER_RECORDS = "order_records"

# =============================================================================
# MongoDB Configuration
# =============================================================================

MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_PORT = int(os.getenv("MONGO_PORT", "27017"))

# MongoDB Database Names
MONGO_DB_QUICKBASKET = "quickbasket"

# MongoDB Collection Names
MONGO_COLLECTION_CHAT_LOGS = "chat_logs"
MONGO_COLLECTION_ORDER_LOGS = "order_logs"

# =============================================================================
# Application Configuration
# =============================================================================

# PDF Settings
PDF_FOLDER = "OrderPDF"

# Webhook URLs (from environment)
WEBHOOK_TEST_URL = os.getenv("WEBHOOK_TEST_URL", "")
WEBHOOK_PRO_URL = os.getenv("WEBHOOK_PRO_URL", "")

# Application Settings
APP_HOST = os.getenv("APP_HOST", "0.0.0.0")
APP_PORT = int(os.getenv("APP_PORT", "8001"))
