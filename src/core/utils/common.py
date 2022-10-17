import random
import string
from typing import Any
from uuid import UUID

default_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits


def generate_str(size: int = 6, chars: str = default_chars) -> str:
    return "".join(random.choice(chars) for _ in range(size))


def is_uuid(uuid: Any) -> bool:
    try:
        UUID(uuid).version
        return True
    except ValueError:
        return False
