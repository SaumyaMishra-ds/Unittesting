from logging import error
from flask import Flask, request, jsonify, app


def addition(a, b):
    return (a+b)


def substraction(a, b):
    return(a-b)


def multiply(a, b):
    return(a*b)


def division(a, b):
    r = round(a/b, 2)
    return(r)


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def main():
    a = int(request.form.get('a'))
    b = int(request.form.get('b'))
    #a = 8
    #b = 6
    add = addition(a, b)
    sub = substraction(a, b)
    mult = multiply(a, b)
    div = division(a, b)
    return jsonify(add, sub, mult, div)


if __name__ == "__main__":
    app.run(debug=True)
