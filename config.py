import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

SINGLESTORE_CONFIG = {
    "host": os.getenv("SINGLESTOREDB_HOST"),
    "user": os.getenv("SINGLESTOREDB_USER"),
    "password": os.getenv("SINGLESTOREDB_PASSWORD"),
    "database": os.getenv("SINGLESTOREDB_DATABASE"),
}