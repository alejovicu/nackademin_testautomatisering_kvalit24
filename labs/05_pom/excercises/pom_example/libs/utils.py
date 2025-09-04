import random
import string

def generate_username(prefix: str = "test", length: int = 8) -> str:
    """
    Generate a username with a configurable prefix and a random string.

    Args:
        prefix (str): The prefix for the username (default: "test").
        length (int): Length of the random string to append (default: 8).

    Returns:
        str: A username like "test_ab12cd34".
    """
    random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return f"{prefix}_{random_part}"