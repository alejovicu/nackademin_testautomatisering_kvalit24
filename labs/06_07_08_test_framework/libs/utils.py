import random
import string

# GENERATE USERNAME FOR SIGNUP
def generate_string_with_prefix(prefix: str = "user", length: int = 8) -> str:
    """
    Generate a string with a configurable prefix and a random string.

    Args:
        prefix (str): The prefix for the username (default: "user").
        length (int): Length of the random string to append (default: 8).

    Returns:
        str: A username like "user_ab12cd34".
    """
    random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return f"{prefix}_{random_part}"
