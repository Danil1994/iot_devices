import os

from dotenv import load_dotenv
from peewee import PostgresqlDatabase, SqliteDatabase

load_dotenv()

# db = SqliteDatabase('app.db') <- uncomment if you wont use SQLite DB and comment code below


db = PostgresqlDatabase(
    os.getenv('DATABASE'),
    user='postgres',
    password=os.getenv('DATABASW_PASSWORD'),
    host='localhost',
    port=5432
)
