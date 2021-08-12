import string
import random

def random_string(size):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(size))

def email(name):
    name_array = name.split(' ')
    email = '{0}-{1}.{2}-test@gmail.com'.format(random_string(size=4), name_array[0], name_array[1])
    return email
