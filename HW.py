from flask import Flask
import requests
from faker import Faker


def faker():
    fake = Faker("")
    return {fake.name(): fake.email() for _ in range(10)}



app = Flask("app")


@app.route("/")
def requirements():
    f = open("requirements.txt")
    content = f.read()
    f.close()
    return content


if __name__ == "__main__":
    app.run()

def file():
    f = open("hw.csv")
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
    return (height_sum / number) * 2.54, (weight_sum / number) * 0.454


def kosmos():
    kosmos = requests.get("http://api.open-notify.org/astros.json")
    p = kosmos.text
    return p.count("name")

