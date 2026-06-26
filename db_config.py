import os
import psycopg2
from dotenv import load_dotenv

# Load variables from the .env file in the root directory
load_dotenv()

def get_db_connection():
    try:
        connection = psycopg2.connect(
            user=os.getenv("DB_USER"),
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )
        return connection
    except Exception as error:
        print(f"❌ Error connecting to database: {error}")
        return None
