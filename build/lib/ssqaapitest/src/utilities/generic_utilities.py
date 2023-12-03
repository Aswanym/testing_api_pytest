import logging as logger
import random
import string

def generate_random_email_and_password(domain=None, email_prefix=None):
    logger.debug("Generating random email and password")

    if not domain:
        domain = 'example.com'

    if not email_prefix:
        email_prefix = 'testuser'

    random_email_length = 10
    random_email_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_length))
    email = f"{email_prefix}_{random_email_string}@{domain}"

    random_password_length = 20
    random_password_string = ''.join(random.choices(string.ascii_letters, k=random_password_length))

    random_info = {
        'email': email,
        'password': random_password_string
    }
    logger.info(f"Randomly generated email and password: {random_info}")

    return random_info
