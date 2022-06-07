import random
import string
from faker import Faker


# using Faker to generate addresses
def generate_address(amount: int):
    fake = Faker()
    block = ''
    for _ in range(amount):
        chars = string.ascii_letters + string.digits
        address = ''

        for _ in range(random.randrange(4, 9, 1)):
            address += random.choice(chars)

        line = fake.unique.first_name() + ' ' + address + '@mail.com'
        block += line + "\n"
    return block
