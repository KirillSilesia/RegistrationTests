import random
import string

specials = ["!", "?", "%", "$", "#", "}", "^", "&"]

def random_email_special(specials_length=7, letters_length=4):
    letters = string.ascii_letters
    first_part = ''.join(random.choice(specials) for _ in range(specials_length))
    return f"{first_part}@knowlee.pl"

email_random_emojis = random_email_special()

def random_email_no_domain(length=7):
    letters = string.ascii_letters
    first_part = ''.join(random.choice(letters) for i in range(length))
    return f"{first_part}@knowlee"

email_random_no_domain = random_email_no_domain()

def random_email_double_at(length=7):
    letters = string.ascii_letters
    first_part = ''.join(random.choice(letters) for i in range(length))
    return f"{first_part}@@knowlee.pl"

email_random_double_at = random_email_double_at()

def random_email(length=7):
    letters = string.ascii_letters
    first_part = ''.join(random.choice(letters) for i in range(length))
    return f"{first_part}@knowlee.pl"

email_random = random_email()

def random_email_without_at(length=7):
    letters = string.ascii_letters
    first_part = ''.join(random.choice(letters) for i in range(length))
    return f"{first_part}knowlee.pl"

email_random_without_at = random_email_without_at()