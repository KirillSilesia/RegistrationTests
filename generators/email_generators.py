import random
import string

specials = ["!", "?", "%", "$", "#", "}", "^", "&"]

def random_email_special(specials_length=7, letters_length=4):
    letters = string.ascii_letters
    first_part = ''.join(random.choice(specials) for _ in range(specials_length))
    second_part = ''.join(random.choice(letters) for _ in range(letters_length))
    return f"{first_part}@{second_part}.com"

email_random_emojis = random_email_special()

def random_email_no_domen(length=7):
    letters = string.ascii_letters
    first_part = ''.join(random.choice(letters) for i in range(length))
    second_part = ''.join(random.choice(letters) for i in range(length))
    return f"{first_part}@{second_part}"

email_random_no_domen = random_email_no_domen()

def random_email_double_at(length=7):
    letters = string.ascii_letters
    first_part = ''.join(random.choice(letters) for i in range(length))
    second_part = ''.join(random.choice(letters) for i in range(length))
    return f"{first_part}@@{second_part}.com"

email_random_double_at = random_email_double_at()

def random_email(length=7):
    letters = string.ascii_letters
    first_part = ''.join(random.choice(letters) for i in range(length))
    second_part = ''.join(random.choice(letters) for i in range(length))
    return f"{first_part}@{second_part}.com"

email_random = random_email()

def random_email_without_at(length=7):
    letters = string.ascii_letters
    first_part = ''.join(random.choice(letters) for i in range(length))
    return f"{first_part}.com"

email_random_without_at = random_email_without_at()