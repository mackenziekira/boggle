import string
import random

def render_board():
    """returns a list of five lists, each with five random letters

    >>> render_board() # doctest: +ELLIPSIS
    [[...], [...], [...], [...], [...]]
    """

    alphabet = string.letters
    board = [[random.choice(alphabet).upper() for letter in xrange(5)] for row in xrange(5)]
    return board