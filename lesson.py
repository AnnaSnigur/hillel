import string
from flask import Flask
import random
from hillel.query import exec_query

app = Flask("app")


@app.route("/gen")
def gen():
    from flask import request
    p = request.args['len']
    if not p.isdigit() or len(p) > 3:
        return "Error"
    return ''.join(
        random.choice(string.ascii_uppercase) for i in range(int(p))
    )


@app.route("/all-customers")
def all_customers():
    from flask import request
    query = f'SELECT * FROM  customers WHERE State = \'{request.args["State"]}\' AND City = \'{request.args["City"]}\';'
    result = exec_query(query)
    return str(result)


@app.route("/count-name")
def count_name():
    query = 'SELECT FirstName, COUNT(FirstName) FROM Customers GROUP BY FirstName;'
    result = exec_query(query)
    return str(result)


@app.route("/revenue")
def revenue():
    query = 'SELECT SUM(UnitPrice*Quantity) FROM invoice_items;'
    result = exec_query(query)
    return str(result)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
