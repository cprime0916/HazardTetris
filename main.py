# Python STL
import sys
import pygame
import random


# Self-made Package
import const
from tetris import *
from data import *  # database lib
import ui


# Time Package
import time
import datetime


# set Difficulty
diff = const.diff


# Screen Start
pygame.init()


# SQL Database
db = Data()  # db = Database
name = "test"

# Text for text
def draw_text(screen, text, x, y):
    font = pygame.font.Font(None, 36)  # FontSize Settings
    text = font.render(text, True, WHITE)  # Text Content
    screen.blit(text, (x, y))
    pygame.display.flip()

# Erase Content in the Middle
def erase(screen, x, y):
    pygame.draw.rect(screen, (0, 0, 0), (x, y, 30, 30))
    pygame.display.flip()
# Text for score
def draw_score(screen, score, x, y):
    """Draw the score on the screen"""
    font = pygame.font.Font(None, 36)  # FontSize Settings
    text = font.render(f"Score: {score}", True, WHITE)  # Text Content
    screen.blit(text, (x, y))  # Show Text

# Text for Game Over
def draw_game_over(screen, x, y):
    """Draw the game over text on the screen"""
    font = pygame.font.Font(None, 48)  # FontS ize Settings
    text = font.render("Game Over", True, RED)  # Text Content
    screen.blit(text, (x, y))  # Show Text


# Build Hazard Functions

def hazards(screen, x, y):
    global WIND, SNOWING, TYPHOON, EARTHQUAKE

    if not (WIND[0] or TYPHOON[0] or EARTHQUAKE): # If there is no hazard currently
        randnum = random.randint(1, 50)  # Choose Hazard Event
        if randnum == 1:  # 1/7 Chance
            WIND[0] = True  # Wind Start
            WIND[1] = random.choice(["Left", "Right"])  # Set direction of wind, 1/2 Chance for both direction

        elif randnum == 50:  # 1/7 Chance
            TYPHOON[0] = True  # Typhoon Start
    if not SNOWING[0]:
        randnum = random.randint(1, 300)
        if randnum == 1:
            SNOWING[0] = True

    # Show Current Hazard Event
    font = pygame.font.Font(None, 36)
    text = font.render("Peaceful", True, WHITE)
    if WIND[0]:
        text = font.render("Windy", True, BLUE)
    elif SNOWING[0]:
        text = font.render("Snowy", True, WHITE)
    elif TYPHOON[0]:
        text = font.render("Typhoon", True, BLUE)

    # Show Text
    screen.blit(text, (x, y))


def main(diff):
    print(f"{diff}")
    game = Tetris(WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE, diff)  # Game initialize
    # Initialize pygame
    screen = const.screen  # Show screen
    pygame.display.set_caption('Tetris')  # Screen Title

    # Create Game Clock
    clock = pygame.time.Clock()

    keys = pygame.key.get_pressed()  # Detect which key is pressed during every frame

    # Change of falling speed according to the argument fall_speed
    fall_time = 0
    if diff == "Beginner":
        fall_speed = 120
    elif diff == "Easy":
        fall_speed = 80
    elif diff == "Normal":
        fall_speed = 50
    elif diff == "Hard":
        fall_speed = 40
    elif diff == "Glitch":  # when I chose asian, it uses mode "Glitch" instead
        fall_speed = 25
    elif diff == "StMarks":
        fall_speed = 12
    else:
        fall_speed = 50  # You can adjust this value to change the falling speed, it's in milliseconds

    ### Settings end

    screen.fill(BLACK)
    # 3 secs COUNTDOWN
    draw_text(screen, "3.", WIDTH // 2, HEIGHT // 2)
    time.sleep(1)
    erase(screen, WIDTH // 2, HEIGHT // 2)
    draw_text(screen, "2..", WIDTH // 2, HEIGHT // 2)
    time.sleep(1)
    erase(screen, WIDTH // 2, HEIGHT // 2)
    draw_text(screen, "1...", WIDTH // 2, HEIGHT // 2)
    time.sleep(1)
    erase(screen, WIDTH // 2, HEIGHT // 2)
    draw_text(screen, "GO!", WIDTH // 2, HEIGHT // 2)
    time.sleep(0.5)
    erase(screen, WIDTH // 2, HEIGHT // 2)

    # Timer
    start_time = datetime.datetime.now()

    # SMS png
    # image = pygame.image.load("stmarks.png")
    IMAGE_X = 450
    IMAGE_Y = 200
    # Game start
    while True:

        # Fill background color to black
        screen.fill(BLACK)
        pygame.draw.rect(screen, (125, 125, 125), (0, 0, 1000, 1000))
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 250, 500))
        # screen.blit(image, (IMAGE_X, IMAGE_Y))
        # pygame.display.flip()

        # For every action we get from the game
        for event in pygame.event.get():

            # Check for the QUIT event
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Actions that need to be checked if the game is running
            if not game.game_over:

                # Check if keys are pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        if game.valid_move(game.current_piece, -1, 0, 0):
                            game.current_piece.x -= 1  # Move the piece to the left
                        if WIND[1] or TYPHOON[1]:
                            if game.valid_move(game.current_piece, -1, 0, 0):
                                if random.randint(0, 1) == 0:
                                    game.current_piece.x -= 1  # Move the piece to the left
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if game.valid_move(game.current_piece, 1, 0, 0):
                            game.current_piece.x += 1  # Move the piece to the right
                        if WIND[2] or TYPHOON[1]:
                            if game.valid_move(game.current_piece, 1, 0, 0):
                                if random.randint(0, 1) == 0:
                                    game.current_piece.x += 1  # Move the piece to the left
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if game.valid_move(game.current_piece, 0, 1, 0):
                            game.current_piece.y += 1  # Move the piece down
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        if game.valid_move(game.current_piece, 0, 0, 1):
                            # game.rotate_sound.play()
                            game.current_piece.rotation += 1  # Rotate the piece
                    if event.key == pygame.K_SPACE:
                        while game.valid_move(game.current_piece, 0, 1, 0):
                            game.current_piece.y += 1  # Move the piece down until it hits the bottom
                        game.lock_piece(game.current_piece)  # Lock the piece in place

        # Get the number of milliseconds since the last frame
        delta_time = clock.get_rawtime()

        # Add the delta time to the fall time
        fall_time += delta_time
        
        # If it is time for gravity to run 
        if fall_time >= fall_speed:

            # Move the piece down
            game.update()

            # Reset the fall time
            fall_time = 0

        # Draw the score on the screen
        draw_score(screen, game.score, 10, 10)

        # Update Hazard States
        hazards(screen, 10, 30)

        # Time Count (unit=60s)

        current_time = datetime.datetime.now()
        passed_time = current_time-start_time
        passed_time_in_sec = round(passed_time.total_seconds(), 2)
        # Time Check
        if passed_time_in_sec > 60:
            game.game_over = True # Game Over!

        # Update timer's time
        if not game.game_over:
            timer_font = pygame.font.Font(None, 36)
            timer_text = f"Time: {passed_time_in_sec:.2f}"

        # Display Timer
        timer_surface = timer_font.render(timer_text, True, WHITE)
        timer_rect = timer_surface.get_rect()
        timer_rect.center = (WIDTH // 2 - 53, HEIGHT // 2 - 180)
        pygame.draw.rect(screen, BLACK, timer_rect)
        screen.blit(timer_surface, timer_rect)
        # Draw the grid and the current piece
        game.draw(screen)

        # If the game ends...
        if game.game_over:

            # Draw the "Game Over" message
            draw_game_over(screen, WIDTH // 2 - 100, HEIGHT // 2 - 30)  # Draw the "Game Over" message

            # You can add a "Press any key to restart" message here
            if event.type == pygame.KEYDOWN:

                # Only Button R resets the game
                if event.key == pygame.K_r:
                    start_menu_main()
                    # game = Tetris(WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE)


        # Update the display
        pygame.display.flip()

        # Set the framerate
        clock.tick(60)


def start_menu_main():
    global diff


    # Initialize Pygame
    pygame.init()

    # Set up the window
    screen_height = HEIGHT
    window = pygame.display.set_mode((WIDTH, screen_height), pygame.FULLSCREEN)
    pygame.display.set_caption("Start Menu")

    # Set up the font
    font = pygame.font.Font(None, 25)

    # Basic button coordinates
    button_x = (WIDTH - BUTTON_WIDTH) // 2
    button_y = (screen_height - BUTTON_HEIGHT) // 2

    # Construction of Beginner object
    noob_button_x = (WIDTH - BUTTON_WIDTH) // 2
    noob_button_y = (screen_height - BUTTON_HEIGHT + 2*NOOB_Y) // 2
    Beginner = ui.Button(noob_button_x, noob_button_y, "Beginner")

    # Construction of Easy object
    easy_button_x = (WIDTH - BUTTON_WIDTH) // 2
    easy_button_y = (screen_height - BUTTON_HEIGHT + 2*EASY_Y) // 2
    Easy = ui.Button(easy_button_x, easy_button_y, "Easy")

    # Construction of Normal object
    normal_button_x = (WIDTH - BUTTON_WIDTH) // 2
    normal_button_y = (screen_height - BUTTON_HEIGHT + 2*NORMAL_Y) // 2
    Normal = ui.Button(normal_button_x, normal_button_y, "Normal")

    # Construction of Hard object
    hard_button_x = (WIDTH - BUTTON_WIDTH) // 2
    hard_button_y = (screen_height - BUTTON_HEIGHT + 2*HARD_Y) // 2
    Hard = ui.Button(hard_button_x, hard_button_y, "Hard")

    # Construction of Glitch object
    glitch_button_x = (WIDTH - BUTTON_WIDTH) // 2
    glitch_button_y = (screen_height - BUTTON_HEIGHT + 2*GLITCH_Y) // 2
    Glitch = ui.Button(glitch_button_x, glitch_button_y, "Glitch")

    # Construction of StMarks object
    asian_button_x = (WIDTH - BUTTON_WIDTH) // 2
    asian_button_y = (screen_height - BUTTON_HEIGHT + 2*ASIAN_Y) // 2
    StMarks = ui.Button(asian_button_x, asian_button_y, "StMarks")

    # Settings End

    # Screen start running
    running = True
    while running:

        # For everything the game detected
        for event in pygame.event.get():

            # Check for the QUIT event
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # If something is clicked
            elif event.type == pygame.MOUSEBUTTONDOWN:

                # Construct Buttons
                Beginner.construct(button_x, button_y + NOOB_Y)
                Easy.construct(button_x, button_y + EASY_Y)
                Normal.construct(button_x, button_y + NORMAL_Y)
                Hard.construct(button_x, button_y + HARD_Y)
                Glitch.construct(button_x, button_y + GLITCH_Y)
                StMarks.construct(button_x, button_y + ASIAN_Y)

                # Check Click
                Beginner.on_press(event, main, diff, "Beginner")
                Easy.on_press(event, main, diff, "Easy")
                Normal.on_press(event, main, diff, "Normal")
                Hard.on_press(event, main, diff, "Hard")
                Glitch.on_press(event, main, diff, "Glitch")
                StMarks.on_press(event, main, diff, "StMarks")

        # Window Color
        window.fill(BLACK)

        # Draw the button
        Beginner.draw()
        Easy.draw()
        Normal.draw()
        Hard.draw()
        Glitch.draw()
        StMarks.draw()

        pygame.display.flip()


if __name__ == "__main__":
    start_menu_main()