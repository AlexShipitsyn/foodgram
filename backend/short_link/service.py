import string
from random import choice, randint

from short_link.constants import MIN, MAX


def generate_hash() -> str:
    """Генератор коротких ссылок."""
    return ''.join(
        choice(string.ascii_letters + string.digits)
        for _ in range(randint(MIN, MAX))
    )
