from peewee import *
from config_db import db
from validator import EmailField


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    name = CharField(max_length=25)
    email = EmailField()
    password = CharField()

    class Meta:
        table_name = 'api_users'


class Location(BaseModel):
    name = CharField(max_length=50)


class Device(BaseModel):
    user_id = ForeignKeyField(User.id, backref='devices')
    location_id = ForeignKeyField(Location.id, backref='devices')

    name = CharField(max_length=50)
    type = CharField(max_length=25)
    login = CharField(max_length=25)
    password = CharField()
