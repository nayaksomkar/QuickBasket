# =============================================================================
# initDB.py - Main Database Initialization Script
# 
# This script initializes both PostgreSQL and MongoDB databases for QuickBasket
# Run this script to set up all required databases, tables, and collections
# =============================================================================

import initPost
import initMongo


def init_all_databases(drop_existing=False):
    """
    Main function to initialize all databases
    
    Parameters:
    - drop_existing (bool): If True, drops existing database/collections and recreates
                           If False, creates only if they don't exist
    """
    
    print("\n" + "#"*60)
    print("# QuickBasket Database Initialization")
    print("#"*60)
    print(f"Drop existing: {drop_existing}")
    
    # Initialize PostgreSQL
    initPost.init_postgres(drop_existing=drop_existing)
    
    # Initialize MongoDB
    initMongo.init_mongodb(drop_existing=drop_existing)
    
    print("="*60)
    print("All databases initialized successfully!")
    print("="*60)


# Run if executed directly
if __name__ == "__main__":
    print("QuickBasket Database Initialization")
    print("="*40)
    choice = input("Drop and recreate all databases? (yes/no): ").strip().lower()
    drop_existing = choice in ['yes', 'y']
    init_all_databases(drop_existing=drop_existing)
