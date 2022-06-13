from flask import Flask, request
from utils import generate_address
import csv


app = Flask('flask_app')


# Starting page
@app.route("/")
def first_page():
    return "Write /requirements/ to open this" \
           "\nOr /generate-users/ using ?amount=..." \
           "\nOr /mean/"


# Outputting requirements.txt
@app.route("/requirements/")
def read_file():
    with open('requirements.txt') as f:
        content = f.read()
        return content


# Generating users + their email's addresses
@app.route("/generate-users/")
def name_user():
    query_params = request.args
    amount = query_params.get('amount') or ''
    default_amount = 50
    min_amount = 10
    max_amount = 100

    if amount.isdigit():
        amount = int(amount)
        if amount > max_amount or amount < min_amount:
            return generate_address(default_amount)
        else:
            return generate_address(amount)


# Working with .csv file
@app.route("/mean/")
def counter():
    file = 'hw.csv'
    with open(file, newline='') as file:
        reader = csv.reader(file, delimiter=',')
        line_count = 0
        block = ''
        for row in reader:
            if line_count == 0:
                block += ', '.join(row)
                line_count += 1
            else:
                block += '\n' + ''.join(row[0]) + ', ' + ''.join(row[1]) + ', ' + ''.join(row[2])
                line_count += 1
            if line_count == 5:
                break
        #print(f'lines: {line_count}')
        print(block)
        return block


if __name__ == '__main__':
    app.run(port=5557)
