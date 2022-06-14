from flask import Flask, request
from utils import generate_address, average_count


app = Flask('flask_app')


# Starting page
@app.route("/")
def first_page():
    return "Write /requirements/ to open this" \
           "    Or /generate-users/ using ?amount=..." \
           "    Or /mean/"


# Outputting requirements.txt
@app.route("/requirements/")
def read_file():
    with open('requirements.txt') as f:
        content = f.read()
        return content


# Generating users + their email's addresses
@app.route("/generate-users/")
def name_user():
    default_amount = 100
    min_amount = 10
    max_amount = 300
    query_params = request.args
    amount = query_params.get('amount') or f'{default_amount}'

    if amount.isdigit():
        amount = int(amount)
        if amount > max_amount or amount < min_amount:
            return generate_address(default_amount)
        else:
            return generate_address(amount)


# Working with .csv file
@app.route("/mean/")
def counter():
    return average_count()


if __name__ == '__main__':
    app.run(port=5557)
