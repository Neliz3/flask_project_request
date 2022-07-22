from flask import Flask, request
from utils import generate_address, average_count
import requests
import sqlite3
from db_create import executing


app = Flask('flask_app')


# Starting page
@app.route("/")
def first_page():
    return "Write /requirements/" \
           "    *** /generate-users/ using ?amount=..." \
           "    *** /mean/" \
           "    *** /space/" \
           "    *** /users/numbers/" \
           "    *** /users/numbers/add/?number=123" \
           "    *** /users/numbers/update/?old_num=123&new_num=000" \
           "    *** /users/numbers/delete/?number_del=000"


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


# Dealing with database
# Adding value to database
@app.route('/users/numbers/add/')
def user_number_add():
    query_params = request.args
    u_number = query_params.get('number') or '0123456789'

    con = sqlite3.connect('phones.db')
    cur = con.cursor()

    sql = f"""
    INSERT INTO phones
    VALUES (null, '{u_number}')"""
    cur.execute(sql)
    con.commit()
    con.close()

    return f"Number: '{u_number}' was added"


# Inserting value from database
@app.route('/users/numbers/')
def numbers_show():

    con = sqlite3.connect('phones.db')
    cur = con.cursor()

    sql = """SELECT * FROM phones"""
    cur.execute(sql)
    users_list = cur.fetchall()
    # breakpoint()
    con.close()
    return str(users_list)


# Updating value in database
@app.route('/users/numbers/update/')
def number_update():
    query_params = request.args
    old_number = query_params.get('old_num') or '0123456789'
    new_number = query_params.get('new_num') or '000'

    sql = f"""UPDATE phones SET value='{new_number}' WHERE value='{old_number}'"""
    sms = f"'{old_number}' was updated to '{new_number}'"
    return executing(old_number, sql, sms)


# Deleting value from database
@app.route('/users/numbers/delete/')
def number_delete():
    query_params = request.args
    number_del = query_params.get('number_del') or '0123456789'

    sql = f"""DELETE FROM phones WHERE value='{number_del}'"""
    sms = f"'{number_del}' was deleted"
    return executing(number_del, sql, sms)


if __name__ == '__main__':
    app.run(port=5557, debug=True)
