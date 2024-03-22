from flask import Flask, abort, redirect, url_for
from flask import request

from cats.entity.cat import Cat
from cats.repository.catRepositoryInMemory import *


app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('find_all'), 301)


@app.route("/add_cat", methods=["POST"])
def add_cat():
    body = request.json
    id = body["id"]
    name = body["name"]
    colour = body["colour"]
    result = Cat(id, name, colour)
    addCat(result)
    return f"cat {result} added to data base"


@app.route("/find_by_name/<string:cat_name>", methods=["GET"])
def find_by_name(cat_name):
    result = findCatByName(cat_name)
    if result is None:
        abort(404)
    return result.to_json()


@app.route("/find_all", methods=["GET"])
def find_all():
    result = list()
    for cat in cats:
        result.append(cat.to_json())
    return result


def start():
    app.run(port=8080)
