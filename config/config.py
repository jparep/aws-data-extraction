import os
import from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# AWS PostgreSQL database configuration
DB_CONFIG = {
    "DB_TYPE": "postgresql",
    "DB_DRIVER": "psycopg2",
    "HOST": os.getenv("AWS_DB_HOST"),
    "DATABASE": os.getenv("AWS_DB_NAME"),
    "USER": os.getenv("AWS_DB_USER"),
    "PASSWORD": os.getenv("AWS_DB_PASSWORD"),
    "PORT": os.getenv("AWS_DB_PORT"),
}

# Database filtering parameters
DATA_START_DATE = os.getenv("DATA_START_DATE")
DATA_LIMIT = os.getenv("DATA_LIMIT")