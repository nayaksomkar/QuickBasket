# =============================================================================
# initMongo.py - MongoDB Database Initialization
# 
# This script initializes MongoDB database with required collections
# =============================================================================

import pymongo
import config


def init_mongodb(drop_existing=False):
    """
    Initialize MongoDB database with required collections
    
    Parameters:
    - drop_existing (bool): If True, drops existing collections and recreates
                           If False, creates collections only if they don't exist
    """
    
    print("\n" + "="*60)
    print("Initializing MongoDB Database")
    print("="*60)
    
    # Connect to MongoDB
    client = pymongo.MongoClient(
        host=config.MONGO_HOST,
        port=config.MONGO_PORT
    )
    
    # Select quickbasket database
    db = client[config.MONGO_DB_QUICKBASKET]
    
    if drop_existing:
        # Drop collections if they exist
        if config.MONGO_COLLECTION_CHAT_LOGS in db.list_collection_names():
            db[config.MONGO_COLLECTION_CHAT_LOGS].drop()
        if config.MONGO_COLLECTION_ORDER_LOGS in db.list_collection_names():
            db[config.MONGO_COLLECTION_ORDER_LOGS].drop()
        print("Dropped existing collections (fresh)")
    
    # Create or get chat_logs collection
    chat_logs = db[config.MONGO_COLLECTION_CHAT_LOGS]
    chat_logs_exists = config.MONGO_COLLECTION_CHAT_LOGS in db.list_collection_names()
    
    if drop_existing or not chat_logs_exists:
        # Create index
        chat_logs.create_index("timestamp")
        print(f"Collection '{config.MONGO_COLLECTION_CHAT_LOGS}' created")
    else:
        print(f"Collection '{config.MONGO_COLLECTION_CHAT_LOGS}' already exists (skipping)")
    
    # Create or get order_logs collection
    order_logs = db[config.MONGO_COLLECTION_ORDER_LOGS]
    order_logs_exists = config.MONGO_COLLECTION_ORDER_LOGS in db.list_collection_names()
    
    if drop_existing or not order_logs_exists:
        # Create indexes
        order_logs.create_index("order_id")
        order_logs.create_index("timestamp")
        print(f"Collection '{config.MONGO_COLLECTION_ORDER_LOGS}' created")
    else:
        print(f"Collection '{config.MONGO_COLLECTION_ORDER_LOGS}' already exists (skipping)")
    
    client.close()
    
    print("MongoDB initialization completed\n")


# Run if executed directly
if __name__ == "__main__":
    print("MongoDB Initialization")
    print("="*40)
    choice = input("Drop and recreate collections? (yes/no): ").strip().lower()
    drop_existing = choice in ['yes', 'y']
    init_mongodb(drop_existing=drop_existing)
