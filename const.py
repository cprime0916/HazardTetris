import pygame
# width and height
WIDTH, HEIGHT = 500, 500
GRID_SIZE = 25
BUTTON_WIDTH = 50
BUTTON_HEIGHT = 20
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BROWN = (107, 0, 7)
COLORS = [RED, BLUE, GREEN]
GRAVITY = 10
# self.diff = "Easy"
WIND = [False, "Left", 0]
WATER = False
TYPHOON = [False, 0]
SNOWING = [False, 0]
EARTHQUAKE = False
VOLCANIC = [False, 0]
diff = "Noob"
# Read new score
# with open("new_score.txt") as f:
#     highest_score = int(f.readline())
#     f.close()

# screen set-up
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Tetromino shapes

SHAPES = [
    [
        ['.....',
         '.....',
         '.....',
         'OOOO.',
         '.....'],
        ['.....',
         'O....',
         'O....',
         'O....',
         'O....']
    ],
    [
        ['.....',
        '.....',
        'OO...',
        'OO...',
        '.....'],
        ['.....',
        '.....',
        'OO...',
        'OO...',
        '.....']
    ],
    [
        ['.....',
         '.....',
         '.O...',
         'OOO..',
         '.....'],
        ['.....',
         '.O...',
         'OO...',
         '.O...',
         '.....'],
        ['.....',
         '.....',
         'OOO..',
         '.O...',
         '.....'],
        ['.....',
         'O....',
         'OO...',
         'O....',
         '.....']
    ],
    [
        [
         '.....',
         '.....',
         '.OO..',
         'OO...',
         '.....'],
        ['.....',
         'O....',
         'OO...',
         '.O...',
         '.....']
    ],
    [
        ['.....',
         '.....',
         'OO...',
         '.OO..',
         '.....'],
        ['.....',
         '.O...',
         'OO...',
         'O....',
         '.....']
    ],
    [
        ['.....',
         '..O..',
         'OOO..',
         '.....',
         '.....'],
        ['.....',
         'OO...',
         '.O...',
         '.O...',
         '.....'],
        ['.....',
         '.....',
         'OOO..',
         'O....',
         '.....'],
        ['.....',
         'O....',
         'O....',
         'OO...',
         '.....'],
    ],
    [
        [
         '.....',
         'O....',
         'OOO..',
         '.....',
         '.....'],
        ['.....',
         'OO...',
         'O....',
         'O....',
         '.....'],
        ['.....',
         '.....',
         'OOO..',
         '..O..',
         '.....'],
        ['.....',
         '.O...',
         '.O...',
         'OO...',
         '.....'],
    ],
]