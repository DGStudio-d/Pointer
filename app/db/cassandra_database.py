from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from app.core.config import settings
from app.models.cassandra_models import CASSANDRA_TABLES

cluster = None
session = None

def get_cassandra_session():
    global cluster, session
    if session is None:
        hosts = settings.CASSANDRA_HOSTS.split(',')
        cluster = Cluster(hosts, port=settings.CASSANDRA_PORT)
        session = cluster.connect()
    return session

def init_cassandra_db():
    global session
    session = get_cassandra_session()
    
    # Create keyspace if not exists
    session.execute(f"""
        CREATE KEYSPACE IF NOT EXISTS {settings.CASSANDRA_KEYSPACE}
        WITH replication = {{'class': 'SimpleStrategy', 'replication_factor': 1}}
    """)
    
    session.set_keyspace(settings.CASSANDRA_KEYSPACE)
    
    # Create all tables
    for table_name, create_statement in CASSANDRA_TABLES.items():
        try:
            session.execute(create_statement)
            print(f"Created/verified table: {table_name}")
        except Exception as e:
            print(f"Error creating table {table_name}: {e}")
    
    print("Cassandra Database initialized")

def close_cassandra_connection():
    global cluster, session
    if session:
        session.shutdown()
    if cluster:
        cluster.shutdown()
