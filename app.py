from flask import Flask, request
from utils import generate_address, average_count
import requests
import sqlite3


app = Flask('flask_app')


# Starting page
@app.route("/")
def first_page():
    return "Write /requirements/" \
           "    *** /generate-users/ using ?amount=..." \
           "    *** /mean/" \
           "    *** /space/" \
           "    *** /users/number/"


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


# Getting data from .json file with key = 'number'
@app.route("/space/")
def number_astronauts():
    r = requests.get('http://api.open-notify.org/astros.json')
    a = r.json()
    data = str(a['number'])
    amount = f'Amount of astronauts in space is {data}'
    return amount


@app.route('/users/number/')
def users_number():
    con = sqlite3.connect('phones.db')
    cur = con.cursor()
    sql = """
    INSERT INTO phones
    VALUES (null, 0123456789)"""
    cur.execute(sql)
    con.commit()
    con.close()

    return 'users_number'


if __name__ == '__main__':
    app.run(port=5557, debug=True)
