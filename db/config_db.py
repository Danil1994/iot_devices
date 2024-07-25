from peewee import PostgresqlDatabase


db = PostgresqlDatabase(
    'iot',
    user='postgres',
    password='secret',
    host='localhost',
    port=5432
)
