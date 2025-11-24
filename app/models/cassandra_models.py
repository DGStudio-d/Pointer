"""
Cassandra table definitions
These are created via CQL statements in cassandra_database.py
"""

CASSANDRA_TABLES = {
    "users": """
        CREATE TABLE IF NOT EXISTS users (
            id UUID PRIMARY KEY,
            username TEXT,
            email TEXT,
            hashed_password TEXT,
            phone TEXT,
            role TEXT,
            is_active BOOLEAN,
            created_at TIMESTAMP,
            updated_at TIMESTAMP
        )
    """,
    
    "addresses": """
        CREATE TABLE IF NOT EXISTS addresses (
            id UUID PRIMARY KEY,
            user_id UUID,
            street TEXT,
            city TEXT,
            state TEXT,
            postal_code TEXT,
            country TEXT,
            latitude FLOAT,
            longitude FLOAT,
            is_default BOOLEAN,
            created_at TIMESTAMP
        )
    """,
    
    "drivers": """
        CREATE TABLE IF NOT EXISTS drivers (
            id UUID PRIMARY KEY,
            user_id UUID,
            license_number TEXT,
            vehicle_type TEXT,
            vehicle_number TEXT,
            is_available BOOLEAN,
            rating FLOAT,
            total_deliveries INT,
            created_at TIMESTAMP
        )
    """,
    
    "categories": """
        CREATE TABLE IF NOT EXISTS categories (
            id UUID PRIMARY KEY,
            name TEXT,
            description TEXT,
            image_url TEXT,
            is_active BOOLEAN,
            created_at TIMESTAMP
        )
    """,
    
    "products": """
        CREATE TABLE IF NOT EXISTS products (
            id UUID PRIMARY KEY,
            category_id UUID,
            name TEXT,
            description TEXT,
            price FLOAT,
            image_url TEXT,
            stock INT,
            is_available BOOLEAN,
            rating FLOAT,
            created_at TIMESTAMP,
            updated_at TIMESTAMP
        )
    """,
    
    "orders": """
        CREATE TABLE IF NOT EXISTS orders (
            id UUID PRIMARY KEY,
            user_id UUID,
            driver_id UUID,
            delivery_address_id UUID,
            status TEXT,
            total_amount FLOAT,
            delivery_fee FLOAT,
            notes TEXT,
            created_at TIMESTAMP,
            updated_at TIMESTAMP,
            delivered_at TIMESTAMP
        )
    """,
    
    "order_items": """
        CREATE TABLE IF NOT EXISTS order_items (
            id UUID PRIMARY KEY,
            order_id UUID,
            product_id UUID,
            quantity INT,
            price FLOAT
        )
    """,
    
    "payments": """
        CREATE TABLE IF NOT EXISTS payments (
            id UUID PRIMARY KEY,
            order_id UUID,
            amount FLOAT,
            payment_method TEXT,
            transaction_id TEXT,
            status TEXT,
            created_at TIMESTAMP
        )
    """,
    
    "reviews": """
        CREATE TABLE IF NOT EXISTS reviews (
            id UUID PRIMARY KEY,
            user_id UUID,
            product_id UUID,
            rating INT,
            comment TEXT,
            created_at TIMESTAMP
        )
    """,
    
    "notifications": """
        CREATE TABLE IF NOT EXISTS notifications (
            id UUID PRIMARY KEY,
            user_id UUID,
            title TEXT,
            message TEXT,
            is_read BOOLEAN,
            created_at TIMESTAMP
        )
    """,
    
    "settings": """
        CREATE TABLE IF NOT EXISTS settings (
            id UUID PRIMARY KEY,
            key TEXT,
            value TEXT,
            description TEXT,
            updated_at TIMESTAMP
        )
    """
}
