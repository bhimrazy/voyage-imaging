import logging
import random
import string

logger = logging.getLogger(__name__)
ALPHA_NUM = string.ascii_letters + string.digits


def generate_random_alphanum(length: int = 20) -> str:
    """Generate a random alphanumeric string of length `length`"""
    return "".join(random.choices(ALPHA_NUM, k=length))

