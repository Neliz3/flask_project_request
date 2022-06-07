from flask import Flask, request
from utils import generate_address


app = Flask('flask_app')


# Starting page
@app.route("/")
def first_page():
    return "Write /requirements/ to open this" \
           "\nOr write /generate-users/"


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


if __name__ == '__main__':
    app.run(port=5555)
