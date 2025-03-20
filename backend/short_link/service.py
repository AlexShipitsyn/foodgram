import string
from random import choice, randint

from foodgram.constants import MAX_RANGE, MIN_RANGE


def generate_hash() -> str:
    """Генератор коротких ссылок."""
    return ''.join(
        choice(string.ascii_letters + string.digits)
        for _ in range(randint(MIN_RANGE, MAX_RANGE))
    )
