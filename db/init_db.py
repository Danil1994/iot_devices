from db.config_db import db
from db.models import Device, Location, User


def initialize_database():
    db.connect()
    db.create_tables([User, Location, Device], safe=True)
    db.close()
