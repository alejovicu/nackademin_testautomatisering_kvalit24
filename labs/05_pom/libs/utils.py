import random
import string

def generate_username():
    return "user_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))

def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=10))
