import random
import string


def generate_string_with_prefix(prefix: str = "user", length: int = 8) -> str:
    """
    Generate a string with a configurable prefix and a random string.

    Args:
        prefix (str): The prefix for the username (default: "user").
        length (int): Length of the random string to append (default: 8).

    Returns:
        str: A username like "user_ab12cd34".
    """
    random_part = "".join(
        random.choices(string.ascii_lowercase + string.digits, k=length)
    )
    return f"{prefix}_{random_part}"


def generate_product_string_with_prefix(
    prefix: str = "product", length: int = 8
) -> str:
    """
    Generate a product name with a configurable prefix and a random string.

    Args:
        prefix (str): The prefix for the product name (default: "product").
        length (int): Length of the random string to append (default: 8).

    Returns:
        str: A product name like "product_ab12cd34".
    """
    return generate_string_with_prefix(prefix, length)
