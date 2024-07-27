import os

from dotenv import load_dotenv
from peewee import PostgresqlDatabase

load_dotenv()

db = PostgresqlDatabase(
    os.getenv('DATABASE', 'iot'),
    user=os.getenv('DATABASE_USER', 'postgres'),
    password=os.getenv('DATABASE_PASSWORD', 'secret'),
    host=os.getenv('DATABASE_HOST', 'db'),
    port=5432
)
