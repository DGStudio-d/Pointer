# Pointer Backend API

FastAPI backend with support for both SQL (PostgreSQL) and Cassandra databases.

## Features

- FastAPI framework
- Dual database support (SQL/Cassandra)
- User management endpoints
- CORS enabled
- Environment-based configuration

## Setup

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment:
```bash
cp .env.example .env
# Edit .env with your database credentials
```

4. Run the server:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Database Configuration

### SQL (PostgreSQL)
Set in `.env`:
```
DATABASE_TYPE=sql
SQL_DATABASE_URL=postgresql://user:password@localhost:5432/pointer_db
```

### Cassandra
Set in `.env`:
```
DATABASE_TYPE=cassandra
CASSANDRA_HOSTS=localhost
CASSANDRA_PORT=9042
CASSANDRA_KEYSPACE=pointer_keyspace
```

## API Endpoints

### General
- `GET /` - Root endpoint
- `GET /health` - Health check
- `GET /docs` - Swagger documentation

### Users
- `POST /api/v1/users/` - Create user
- `GET /api/v1/users/` - List users
- `GET /api/v1/users/{user_id}` - Get user by ID

### Products
- `POST /api/v1/products/` - Create product
- `GET /api/v1/products/` - List products
- `GET /api/v1/products/{product_id}` - Get product
- `PUT /api/v1/products/{product_id}` - Update product
- `DELETE /api/v1/products/{product_id}` - Delete product

### Categories
- `POST /api/v1/categories/` - Create category
- `GET /api/v1/categories/` - List categories
- `GET /api/v1/categories/{category_id}` - Get category

### Orders
- `POST /api/v1/orders/` - Create order
- `GET /api/v1/orders/` - List orders
- `GET /api/v1/orders/{order_id}` - Get order

## Project Structure

```
Backend/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── endpoints/
│   │       │   └── users.py
│   │       └── router.py
│   ├── core/
│   │   └── config.py
│   ├── db/
│   │   ├── cassandra_database.py
│   │   ├── sql_database.py
│   │   └── init_db.py
│   ├── models/
│   │   └── sql_models.py
│   └── schemas/
│       └── user.py
├── main.py
├── requirements.txt
└── .env.example
```
