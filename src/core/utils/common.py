import random
import string
from uuid import UUID

default_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits


def generate_str(size=6, chars=default_chars):
    return "".join(random.choice(chars) for _ in range(size))


def is_uuid(uuid):
    try:
        UUID(uuid).version
        return True
    except ValueError:
        return False
