from flask import Flask
from flask import request

import game


app = Flask(__name__)


@app.route("/start_game", methods=["GET"])
def startGame():
    game.startGame()
    return game.boardToString()


@app.route("/make_move", methods=["POST"])
def make_move():
    body = request.json
    row = body["row"]
    col = body["col"]
    cell = body["cell"]
    game.make_move(row, col, cell)
    return game.boardToString()


@app.route("/board", methods=["GET"])
def board():
    return game.boardToString()


@app.route("/status", methods=["GET"])
def status():
    return game.status()


if __name__ == "__main__":
    app.run(port=8080)
