import os
from dotenv import load_dotenv
from psycopg2 import connect

# Load environment variables from db_settings.env
load_dotenv("db_settings.env")

# Set up database settings
settings = {
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'port': os.getenv('DB_PORT')
}

def connect_to_db():
    return connect(**settings)
