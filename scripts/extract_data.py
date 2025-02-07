# Load libraries
import pandas as pd
from sqlalchemy import create_engine
from config.config import DB_CONFIG, DATA_START_DATE, DATA_LIMIT

# Define the specific health data to extract
HEALTH_DATA_FIELDS = [
    "patient_id",
    "patient_name",
    "dob",  # Date of birth
    "diagnosis",
    "prescription",
    "doctor_id",
    "hospital_branch",
    "created_at"  # Data filtering based on created date
]

def get_database_connection():
    """Establishes a connection to the PostgreSQL database."""
    connection_url = (
        f"{DB_CONFIG['DB_TYPE']}+{DB_CONFIG['DB_DRIVER']}://"
        f"{DB_CONFIG['USER']}:{DB_CONFIG['PASSWORD']}@"
        f"{DB_CONFIG['HOST']}:{DB_CONFIG['PORT']}/{DB_CONFIG['DATABASE']}"
    )