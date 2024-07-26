import random

from config_db import db
from faker import Faker
from models import Device, Location, User

fake = Faker()

rooms = ['Living Room', 'Bedroom', 'Kitchen', 'Bathroom', 'Dining Room', 'Home Office', 'Laundry Room']


def create_fake_user():
    return User.create(
        name=fake.name(),
        email=fake.email(),
        password=fake.password()
    )


def create_fake_location():
    return Location.create(
        name=random.choice(rooms)
    )


def create_fake_device(user: int, location: int):
    return Device.create(
        user_id=user,
        location_id=location,
        name=fake.word(),
        type=fake.word(),
        login=fake.user_name(),
        password=fake.password()
    )


def generate_fake_data(num_users=10, num_locations=5, num_devices_per_user=3):
    db.connect()
    db.create_tables([User, Location, Device])

    locations = [create_fake_location() for _ in range(num_locations)]

    for _ in range(num_users):
        user = create_fake_user()

        for _ in range(num_devices_per_user):
            location = fake.random.choice(locations)
            create_fake_device(user.id, location.id)

    db.close()


if __name__ == '__main__':
    generate_fake_data()
