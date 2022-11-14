from hashlib import sha1
from random import choice
from string import ascii_lowercase


from django.conf import settings


def get_unique_slug():
    code = "".join(
        [
            choice(ascii_lowercase) for _ in range(settings.SHORT_URL_LENGHT)
        ]
    )
    return sha1(code.encode()).hexdigest()[:settings.SHORT_URL_LENGHT]

