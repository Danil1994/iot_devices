import os

from dotenv import load_dotenv
from peewee import PostgresqlDatabase, SqliteDatabase

load_dotenv()

db = SqliteDatabase('app.db')


# db = PostgresqlDatabase(
#     os.getenv('DATABASE'),
#     user='postgres',
#     password=os.getenv('DATABASW_PASSWORD'),
#     host='localhost',
#     port=5432
# )
