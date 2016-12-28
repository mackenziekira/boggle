from flask import Flask, render_template
import string
import random

app = Flask(__name__)

@app.route("/")
def homepage():
    alphabet = string.letters
    rows = [[random.choice(alphabet).upper() for letter in xrange(6)] for row in xrange(6)]
    return render_template('board.html', rows=rows)


if __name__ == "__main__":
    app.debug = True
    app.run()