import random
from const import *

class Tetromino:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = random.choice(COLORS) # You can choose different colors for each shape
        self.rotation = 0

class colour_tetromino:
    def __init__(self, x, y, shape, colour):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = colour
        self.rotation = 0