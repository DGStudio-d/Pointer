from app.core.config import settings

async def init_database():
    if settings.DATABASE_TYPE == "sql":
        from app.db.sql_database import init_sql_db
        init_sql_db()
    elif settings.DATABASE_TYPE == "cassandra":
        from app.db.cassandra_database import init_cassandra_db
        init_cassandra_db()
    else:
        raise ValueError(f"Unsupported database type: {settings.DATABASE_TYPE}")
