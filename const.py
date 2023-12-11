import pygame

# Width and Height
WIDTH, HEIGHT = 250, 500
GRID_SIZE = 25
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 30
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BROWN = (107, 0, 7)
COLORS = [RED, BLUE, GREEN]
GRAVITY = 10

# Initial Hazard Settings
WIND = [False, "Left", 0]
WATER = False
TYPHOON = [False, 0]
SNOWING = [False, 0]
EARTHQUAKE = False
VOLCANIC = [False, 0]

# Types of difficulty
DIFF_TYPE = ["Beginner", "Easy", "Normal", "Hard", "Glitch", "StMarks"]
DIFF_SCORE = [0.5, 1.0, 1.25, 1.5, 1.75, 2.0]
LVL_SCORE = [0, 40, 100, 300, 1200]
# Coordibates of Start Menu Buttons
NOOB_Y = -150
EASY_Y = -90
NORMAL_Y = -30
HARD_Y = 30
GLITCH_Y = 90
ASIAN_Y = 150

# Initial Difficulty
diff = "Normal"

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
         '.OO..',
         '.O...',
         '.....'],
        ['.....',
         '.....',
         'OOO..',
         '.O...',
         '.....'],
        ['.....',
         '.O...',
         'OO...',
         '.O...',
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