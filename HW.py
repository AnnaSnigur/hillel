from flask import Flask
import requests
from faker import Faker

app = Flask('app')


@app.route('/')
def requirements():
    with open('requirements.txt') as f:
        content = f.read()
    return content


@app.route('/faker')
def faker():
    fake = Faker('')
    return {fake.name(): fake.email() for _ in range(10)}


@app.route('/file')
def file():
    with open("hw.csv") as f:
        content = f.read()
    content = content.split("\n")[1:]
    number = 0
    height_sum = 0
    weight_sum = 0
    for row in content:
        if not row:
            continue
        number += 1
        height = float(row.split(",")[1])
        height_sum += height
        weight = float(row.split(",")[2])
        weight_sum += weight
        h = (height_sum / number) * 2.54
        w = (weight_sum / number) * 0.454
        list = [h,w]
    return str(list)


@app.route('/kosmos')
def kosmos():
    kosmos = requests.get('http://api.open-notify.org/astros.json')
    p = kosmos.text
    return str(p.count('name'))


if __name__ == '__main__':
    app.run(port=5000)
