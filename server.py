from flask import Flask, render_template, request
from helper_functions import render_board

app = Flask(__name__)

@app.route("/")
def homepage():
    board = render_board()
    return render_template('board.html', board=board)

@app.route("/guess")
def guess():
    guessed_word = request.args.get('guess')
    return guessed_word




if __name__ == "__main__":
    app.debug = True
    app.run()