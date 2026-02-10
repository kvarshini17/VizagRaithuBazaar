"""
Initialize Database for VizagRaithuBazaar
Works with both SQLite (dev) and PostgreSQL (production)
"""

import os
import sys
from database_config import get_database_connection, get_database_type

def init_database():
    """Initialize database with tables"""
    
    db_type = get_database_type()
    print(f"\n{'='*60}")
    print(f"Initializing {db_type.upper()} Database")
    print('='*60)
    
    conn = get_database_connection()
    cursor = conn.cursor()
    
    try:
        # Drop existing tables (for fresh start)
        print("\n1. Dropping existing tables...")
        cursor.execute("DROP TABLE IF EXISTS orders CASCADE")
        cursor.execute("DROP TABLE IF EXISTS crops CASCADE")
        cursor.execute("DROP TABLE IF EXISTS users CASCADE")
        print("   ✓ Old tables dropped")
        
        # Create users table
        print("\n2. Creating users table...")
        if db_type == 'postgresql':
            cursor.execute("""
                CREATE TABLE users (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    phone_number VARCHAR(15) UNIQUE NOT NULL,
                    role VARCHAR(20) NOT NULL CHECK (role IN ('farmer', 'consumer')),
                    location VARCHAR(100),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
        else:
            cursor.execute("""
                CREATE TABLE users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone_number TEXT UNIQUE NOT NULL,
                    role TEXT NOT NULL CHECK (role IN ('farmer', 'consumer')),
                    location TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
        print("   ✓ Users table created")
        
        # Create crops table
        print("\n3. Creating crops table...")
        if db_type == 'postgresql':
            cursor.execute("""
                CREATE TABLE crops (
                    id SERIAL PRIMARY KEY,
                    farmer_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
                    crop_name VARCHAR(50) NOT NULL,
                    price_per_kg DECIMAL(10,2) NOT NULL,
                    quantity DECIMAL(10,2) NOT NULL,
                    location VARCHAR(100),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
        else:
            cursor.execute("""
                CREATE TABLE crops (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    farmer_id INTEGER,
                    crop_name TEXT NOT NULL,
                    price_per_kg REAL NOT NULL,
                    quantity REAL NOT NULL,
                    location TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (farmer_id) REFERENCES users(id)
                )
            """)
        print("   ✓ Crops table created")
        
        # Create orders table
        print("\n4. Creating orders table...")
        if db_type == 'postgresql':
            cursor.execute("""
                CREATE TABLE orders (
                    id SERIAL PRIMARY KEY,
                    consumer_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
                    crop_id INTEGER REFERENCES crops(id) ON DELETE CASCADE,
                    quantity DECIMAL(10,2) NOT NULL,
                    total_price DECIMAL(10,2) NOT NULL,
                    status VARCHAR(20) DEFAULT 'pending',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
        else:
            cursor.execute("""
                CREATE TABLE orders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    consumer_id INTEGER,
                    crop_id INTEGER,
                    quantity REAL NOT NULL,
                    total_price REAL NOT NULL,
                    status TEXT DEFAULT 'pending',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (consumer_id) REFERENCES users(id),
                    FOREIGN KEY (crop_id) REFERENCES crops(id)
                )
            """)
        print("   ✓ Orders table created")
        
        conn.commit()
        
        print("\n" + "="*60)
        print("✅ Database initialized successfully!")
        print("="*60)
        print(f"\nDatabase type: {db_type}")
        print("Tables created: users, crops, orders")
        print("\nNext step: Run init_realistic_data.py to add demo data")
        print("="*60 + "\n")
        
    except Exception as e:
        conn.rollback()
        print(f"\n❌ Error: {e}")
        sys.exit(1)
    finally:
        conn.close()

if __name__ == "__main__":
    init_database()
