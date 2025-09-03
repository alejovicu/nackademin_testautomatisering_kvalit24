import string
import random


def generate_username(length: int = 8) -> str:
    # Create a random username with letters and numbers.
    # Default length is 8 characters.
    # Example: 'a7x3k9bq'

    letters_and_numbers = string.ascii_lowercase + string.digits
    return "".join(random.choice(letters_and_numbers) for _ in range(length))
