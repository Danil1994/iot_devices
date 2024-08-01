import os

from dotenv import load_dotenv
from peewee import PostgresqlDatabase

load_dotenv()

db = PostgresqlDatabase(
    os.getenv('DATABASE'),
    user=os.getenv('DATABASE_USER'),
    password=os.getenv('DATABASE_PASSWORD'),
    host=os.getenv('DATABASE_HOST'),
    port=5432
)
