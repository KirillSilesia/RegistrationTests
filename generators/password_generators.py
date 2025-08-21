import random
import string

def too_long_password(length=256):
    letters = string.ascii_letters
    first_part = ''.join(random.choice(letters) for i in range(length))
    return first_part

password_too_long = too_long_password()

def too_short_password(length=5):
    letters = string.ascii_letters
    first_part = ''.join(random.choice(letters) for i in range(length))
    return first_part

password_too_short = too_short_password()