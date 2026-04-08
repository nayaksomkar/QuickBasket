# =============================================================================
# initPost.py - PostgreSQL Database Initialization
# 
# This script initializes PostgreSQL database with required tables
# =============================================================================

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import config


def init_postgres(drop_existing=False):
    """
    Initialize PostgreSQL database with required tables
    
    Parameters:
    - drop_existing (bool): If True, drops existing database and recreates
                           If False, creates tables only if they don't exist
    """
    
    print("\n" + "="*60)
    print("Initializing PostgreSQL Database")
    print("="*60)
    
    # Connect to default postgres database
    conn = psycopg2.connect(
        host=config.POSTGRES_HOST,
        database=config.POSTGRES_DB_DEFAULT,
        user=config.POSTGRES_USER,
        password=config.POSTGRES_PASSWORD
    )
    
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    
    if drop_existing:
        # Drop and recreate database
        cursor.execute(f"DROP DATABASE IF EXISTS {config.POSTGRES_DB_QUICKBASKET};")
        cursor.execute(f"CREATE DATABASE {config.POSTGRES_DB_QUICKBASKET};")
        print(f"Database '{config.POSTGRES_DB_QUICKBASKET}' created (fresh)")
    else:
        # Check if database exists
        cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{config.POSTGRES_DB_QUICKBASKET}'")
        if cursor.fetchone():
            print(f"Database '{config.POSTGRES_DB_QUICKBASKET}' already exists (skipping)")
        else:
            cursor.execute(f"CREATE DATABASE {config.POSTGRES_DB_QUICKBASKET};")
            print(f"Database '{config.POSTGRES_DB_QUICKBASKET}' created")
    
    cursor.close()
    conn.close()
    
    # Connect to quickbasket database
    conn = psycopg2.connect(
        host=config.POSTGRES_HOST,
        database=config.POSTGRES_DB_QUICKBASKET,
        user=config.POSTGRES_USER,
        password=config.POSTGRES_PASSWORD
    )
    
    conn.autocommit = True
    cursor = conn.cursor()
    
    # Check if products table exists
    cursor.execute(f"""
        SELECT 1 FROM information_schema.tables 
        WHERE table_name = '{config.POSTGRES_TABLE_PRODUCTS}'
    """)
    products_exists = cursor.fetchone()
    
    if drop_existing or not products_exists:
        if drop_existing:
            cursor.execute(f"DROP TABLE IF EXISTS {config.POSTGRES_TABLE_PRODUCTS};")
        
        # Create products table (name and price only)
        cursor.execute(f"""
            CREATE TABLE {config.POSTGRES_TABLE_PRODUCTS} (
                name VARCHAR(100),
                price INTEGER
            );
        """)
        
        # Insert products data (snacks + icecreams)
        products_data = [
            ('banana chips', 35),
            ('black currant icecream', 70),
            ('butterscotch icecream', 65),
            ('chocolate chip icecream', 65),
            ('chocolate icecream', 60),
            ('cookies and cream', 80),
            ('good day biscuits', 25),
            ('kulfi icecream', 50),
            ('kurkure', 20),
            ('lays classic', 20),
            ('mango icecream', 60),
            ('marie gold biscuits', 30),
            ('namkeen mixture', 30),
            ('pista icecream', 75),
            ('popcorn ready pack', 35),
            ('potato chips', 20),
            ('roasted peanuts', 40),
            ('salted cashews small pack', 60),
            ('strawberry icecream', 55),
            ('vanilla icecream', 50),
        ]
        
        cursor.executemany(
            f"INSERT INTO {config.POSTGRES_TABLE_PRODUCTS} (name, price) VALUES (%s, %s)",
            products_data
        )
        
        print(f"Table '{config.POSTGRES_TABLE_PRODUCTS}' created and populated")
    else:
        print(f"Table '{config.POSTGRES_TABLE_PRODUCTS}' already exists (skipping)")
    
    # Check if temporary_order table exists
    cursor.execute(f"""
        SELECT 1 FROM information_schema.tables 
        WHERE table_name = '{config.POSTGRES_TABLE_TEMP_ORDER}'
    """)
    temp_order_exists = cursor.fetchone()
    
    if drop_existing or not temp_order_exists:
        if drop_existing:
            cursor.execute(f"DROP TABLE IF EXISTS {config.POSTGRES_TABLE_TEMP_ORDER};")
        
        # Create temporary_order table
        cursor.execute(f"""
            CREATE TABLE {config.POSTGRES_TABLE_TEMP_ORDER} (
                order_id INTEGER,
                order_item VARCHAR(100),
                order_quantity INTEGER,
                order_price INTEGER,
                price_item INTEGER
            );
        """)
        
        print(f"Table '{config.POSTGRES_TABLE_TEMP_ORDER}' created")
    else:
        print(f"Table '{config.POSTGRES_TABLE_TEMP_ORDER}' already exists (skipping)")
    
    cursor.close()
    conn.close()
    
    print("PostgreSQL initialization completed\n")


# Run if executed directly
if __name__ == "__main__":
    print("PostgreSQL Initialization")
    print("="*40)
    choice = input("Drop and recreate database? (yes/no): ").strip().lower()
    drop_existing = choice in ['yes', 'y']
    init_postgres(drop_existing=drop_existing)
