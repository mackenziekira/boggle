from flask import Flask, render_template
from helper_functions import render_board

app = Flask(__name__)

@app.route("/")
def homepage():
    board = render_board()
    return render_template('board.html', board=board)




if __name__ == "__main__":
    app.debug = True
    app.run()