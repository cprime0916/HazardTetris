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


# set Difficulty
diff = const.diff


# Screen Start
pygame.init()


# SQL Database
db = Data()  # db = Database
name = "test"


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

    if not (WIND[0] or SNOWING[0] or TYPHOON[0] or EARTHQUAKE): # If there is no hazard currently
        randnum = random.randint(1, 30)  # Choose Hazard Event
        if randnum == 1:  # 1/7 Chance
            WIND[0] = True  # Wind Start
            WIND[1] = random.choice(["Left", "Right"])  # Set direction of wind, 1/2 Chance for both direction
        elif randnum == 2:  # 1/7 Chance
            SNOWING[0] = True  # Snow Start
        elif randnum == 3:  # 1/7 Chance
            TYPHOON[0] = True  # Typhoon Start

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
    game = Tetris(WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE)
    # Initialize pygame
    screen = const.screen  # Show screen
    pygame.display.set_caption('Tetris')  # Screen Title

    # Create Game Clock
    clock = pygame.time.Clock()

    game = Tetris(WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE)  # Game initialize
    keys = pygame.key.get_pressed()  # Detect which key is pressed during every frame

    # Change of falling speed according to the argument fall_speed
    fall_time = 0
    if diff == "Noob":
        fall_speed = 120
    elif diff == "Easy":
        fall_speed = 80
    elif diff == "Normal":
        fall_speed = 50
    elif diff == "Hard":
        fall_speed = 50
    elif diff == "Glitch":  # when I chose asian, it uses mode "Glitch" instead
        fall_speed = 35
    elif diff == "Asian":
        fall_speed = 12
    else:
        fall_speed = 50  # You can adjust this value to change the falling speed, it's in milliseconds

    # Timer 
    endtime = time.time() + 60

    ### Settings end

    # Game start
    while True:

        # Fill background color to black
        screen.fill(BLACK)

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
        if fall_time >= fall_speed:
            # Move the piece down
            game.update()
            # Reset the fall time
            fall_time = 0
        # Draw the score on the screen
        draw_score(screen, game.score, 10, 10)
        hazards(screen, 10, 30)
        # Time Count (unit=60s)

        if endtime < time.time():
            game.game_over = True
        # Draw the grid and the current piece
        game.draw(screen)
        if game.game_over:

            # Draw the "Game Over" message
            draw_game_over(screen, WIDTH // 2 - 100, HEIGHT // 2 - 30)  # Draw the "Game Over" message

            # if game.score > highest_score:
            #     Data.push(name=name, score=game.score)
            #     with open("new_score.txt", "w") as f:
            #         f.write(str(game.score))

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
    window = pygame.display.set_mode((WIDTH, screen_height))
    pygame.display.set_caption("Start Menu")

    # Set up the font
    font = pygame.font.Font(None, 25)

    # Basic button coordinates
    button_x = (WIDTH - BUTTON_WIDTH) // 2
    button_y = (screen_height - BUTTON_HEIGHT) // 2

    # Construction of Noob object
    noob_button_x = (WIDTH - BUTTON_WIDTH) // 2
    noob_button_y = (screen_height - BUTTON_HEIGHT + 2*NOOB_Y) // 2
    Noob = ui.Button(noob_button_x, noob_button_y, "Noob")

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

    # Construction of Asian object
    asian_button_x = (WIDTH - BUTTON_WIDTH) // 2
    asian_button_y = (screen_height - BUTTON_HEIGHT + 2*ASIAN_Y) // 2
    Asian = ui.Button(asian_button_x, asian_button_y, "Asian")

    # Settings End
    running = True
    while running:
        for event in pygame.event.get():

            # Check for the QUIT event
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:

                # Construct Buttons
                Noob.construct(button_x, button_y + NOOB_Y)
                Easy.construct(button_x, button_y + EASY_Y)
                Normal.construct(button_x, button_y + NORMAL_Y)
                Hard.construct(button_x, button_y + HARD_Y)
                Glitch.construct(button_x, button_y + GLITCH_Y)
                Asian.construct(button_x, button_y + ASIAN_Y)

                # Check Click
                Noob.on_press(event, main, diff, "Noob")
                Easy.on_press(event, main, diff, "Easy")
                Normal.on_press(event, main, diff, "Normal")
                Hard.on_press(event, main, diff, "Hard")
                Glitch.on_press(event, main, diff, "Glitch")
                Asian.on_press(event, main, diff, "Asian")

        # Window Color
        window.fill(BLACK)

        # Draw the button
        Noob.draw()
        Easy.draw()
        Normal.draw()
        Hard.draw()
        Glitch.draw()
        Asian.draw()

        pygame.display.flip()


if __name__ == "__main__":
    start_menu_main()
