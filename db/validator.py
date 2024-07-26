import re

from peewee import *


class EmailField(CharField):
    def db_value(self, value):
        if value and not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError("Invalid email address")
        return value
