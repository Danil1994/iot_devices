from config_db import db
from models import User, Location, Device


def initialize_database():
    db.connect()
    db.create_tables([User, Location, Device])


if __name__ == '__main__':
    initialize_database()
