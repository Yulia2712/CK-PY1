import random
import string

def get_random_password() -> str:
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    password = ''.join(random.choice(characters) for i in range(8))

    return password




print(get_random_password())