from flask import Flask, render_template, request
from helper_functions import render_board
from werkzeug.contrib.cache import SimpleCache

app = Flask(__name__)

cache = SimpleCache()

@app.route("/")
def homepage():
    board = render_board()
    return render_template('board.html', board=board)

@app.route("/guess")
def guess():
    guessed_word = request.args.get('guess')

    word = cache.get(guessed_word)

    if not word:
        cache.set(guessed_word, guessed_word, timeout=5 * 60)
        return guessed_word

    return ""


if __name__ == "__main__":
    app.debug = True
    app.run()