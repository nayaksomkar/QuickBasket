# =============================================================================
# Configuration File
# Contains all database and server configuration variables
# =============================================================================

# =============================================================================
# PostgreSQL Configuration
# =============================================================================

POSTGRES_HOST = "localhost"           # PostgreSQL server host
POSTGRES_PORT = 5432                  # PostgreSQL server port
POSTGRES_USER = "postgres"            # PostgreSQL username
POSTGRES_PASSWORD = "pass"           # PostgreSQL password
POSTGRES_DB_DEFAULT = "postgres"     # Default database to connect to

# PostgreSQL Database Names
POSTGRES_DB_QUICKBASKET = "quickbasket"  # Main PostgreSQL database

# PostgreSQL Table Names
POSTGRES_TABLE_PRODUCTS = "products"     # Products table
POSTGRES_TABLE_TEMP_ORDER = "temporary_order"  # Temporary order table
POSTGRES_TABLE_ORDERS = "orders"          # Orders table
POSTGRES_TABLE_ORDER_RECORDS = "order_records"  # Order records table

# =============================================================================
# MongoDB Configuration
# =============================================================================

MONGO_HOST = "localhost"              # MongoDB server host
MONGO_PORT = 27017                    # MongoDB server port

# MongoDB Database Names
MONGO_DB_QUICKBASKET = "quickbasket"  # Main MongoDB database

# MongoDB Collection Names
MONGO_COLLECTION_CHAT_LOGS = "chat_logs"    # Chat logs collection
MONGO_COLLECTION_ORDER_LOGS = "order_logs"  # Order logs collection

# =============================================================================
# Application Configuration
# =============================================================================

# PDF Settings
PDF_FOLDER = "OrderPDF"               # Folder to save generated PDFs

# Webhook URLs
WEBHOOK_TEST_URL = "https://milana-unmagnetised-porter.ngrok-free.dev/webhook-test/aeee492a-4277-47ac-97c5-669ea51ca944"
WEBHOOK_PRO_URL = "https://milana-unmagnetised-porter.ngrok-free.dev/webhook/aeee492a-4277-47ac-97c5-669ea51ca944"

# Application Settings
APP_HOST = "0.0.0.0"                  # Flask/FastAPI host
APP_PORT = 5000                       # Flask/FastAPI port
