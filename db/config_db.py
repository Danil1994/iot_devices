import os

from dotenv import load_dotenv
from peewee import PostgresqlDatabase

load_dotenv()

db = PostgresqlDatabase(
    os.getenv('DATABASE'),
    user='postgres',
    password=os.getenv('DATABASW_PASSWORD'),
    host='localhost',
    port=5432
)
