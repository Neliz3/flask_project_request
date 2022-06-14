import random
import string
from faker import Faker
import csv


# using Faker to generate addresses
def generate_address(amount: int):
    fake = Faker()
    box = ''

    for _ in range(amount):
        chars = string.ascii_letters + string.digits
        address = ''

        # Generating a first part of email
        for _ in range(random.randrange(4, 9, 1)):
            address += random.choice(chars)

        line = fake.unique.first_name() + ' ' + address + '@mail.com'
        box += line + '\n'
    return box


# Average
def average_count():
    file = 'hw.csv'
    with open(file, newline='') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)
        sum_height = 0
        sum_weight = 0
        index = 0

        # Finding sum of height, weight and indexes
        for row in reader:
            sum_height += float(row[1])
            sum_weight += float(row[2])
            index += 1

        # Finding average height in cm and average weight in kg
        average_height = (sum_height / index) * 2.54
        average_weight = (sum_weight / index) / 2.205

        block = 'Average height = ' + str(average_height) +\
                '\nAverage weight = ' + str(average_weight)
        return block
