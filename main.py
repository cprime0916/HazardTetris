# Python STL
import sys
import pygame
import random
# Self-made Package
import const
from tetris import *
from data import *  # database lib

# Time Package
import time

# set diff
diff = const.diff
# change diff
diff = "Noob"
# Score Read
with open("new_score.txt") as f:
    highest_score = int(f.readline())
    f.close()

# Screen Start
pygame.init()
# screen = pygame.display.set_mode((1000, 1000), pygame.FULLSCREEN)

# SQL Database
db = Data() # db = Database
name = "test"

# Time Count (unit=60s)
endtime = time.time() + 60


def draw_score(screen, score, x, y):
    """Draw the score on the screen"""
    font = pygame.font.Font(None, 36) # FontSize Settings
    text = font.render(f"Score: {score}", True, WHITE) # Text Content
    screen.blit(text, (x, y)) # Show Text


def draw_game_over(screen, x, y):
    """Draw the game over text on the screen"""
    font = pygame.font.Font(None, 48) # FontS ize Settings
    text = font.render("Game Over", True, RED) # Text Content
    screen.blit(text, (x, y)) # Show Text


# Build Hazard Functions
'''

Functions:

Wind: 
Snowing
Typhoon
Earthquake

'''


def hazards(screen, x, y):
    global WIND, SNOWING, TYPHOON, EARTHQUAKE

    if not (WIND[0] or SNOWING[0] or TYPHOON[0] or EARTHQUAKE):
        randnum = random.randint(1, 7) # Choose Hazard Event
        if randnum == 1:  # 1/7 Chance
            WIND[0] = True  # Wind Start
            WIND[1] = random.choice(["Left", "Right"]) # Set direction of wind, 1/2 Chance for both direction
        elif randnum == 2:  # 1/7 Chance
            SNOWING[0] = True  # Snow Start
        elif randnum == 3:  # 1/7 Chance
            TYPHOON[0] = True  # Typhoon Start
        elif randnum == 4:  # 1/7 Chance
            EARTHQUAKE = True  # Earthquake Start

    # Show Current Hazard Event
    font = pygame.font.Font(None, 36)
    text = font.render("Peaceful", True, WHITE)
    if WIND[0]:
        text = font.render("Windy", True, BLUE)
    elif SNOWING[0]:
        text = font.render("Snowy", True, WHITE)
    elif TYPHOON[0]:
        text = font.render("Typhoon", True, BLUE)
    elif EARTHQUAKE:
        text = font.render("Earthquake", True, BROWN)

    # Show Text
    screen.blit(text, (x, y))


def main():
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
        fall_speed = 50
    elif diff == "Easy":
        fall_speed = 40
    elif diff == "Normal":
        fall_speed = 30
    elif diff == "Hard":
        fall_speed = 20
    elif diff == "GLITCH":
        fall_speed = 10
    elif diff == "Asian":
        fall_speed = 3
    else:
        fall_speed = 20  # You can adjust this value to change the falling speed, it's in milliseconds

    # Settings end

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
            # elif event.type == pygame.VIDEORESIZE:
            #     pass  # Ignore the resize event
            # Check if keys are pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if game.valid_move(game.current_piece, -1, 0, 0):
                        game.current_piece.x -= 1  # Move the piece to the left
                    if WIND[1] or TYPHOON[1]:
                        if game.valid_move(game.current_piece, -1, 0, 0):
                            if random.randint(0, 1) == 0:
                                game.current_piece.x -= 1  # Move the piece to the left
                if event.key == pygame.K_RIGHT:
                    if game.valid_move(game.current_piece, 1, 0, 0):
                        game.current_piece.x += 1  # Move the piece to the right
                    if WIND[2] or TYPHOON[1]:
                        if game.valid_move(game.current_piece, 1, 0, 0):
                            if random.randint(0, 1) == 0:
                                game.current_piece.x += 1  # Move the piece to the left
                if event.key == pygame.K_DOWN:
                    if game.valid_move(game.current_piece, 0, 1, 0):
                        game.current_piece.y += 1  # Move the piece down
                if event.key == pygame.K_UP:
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

        # Draw the grid and the current piece
        game.draw(screen)
        if game.game_over:
            # Draw the "Game Over" message
            draw_game_over(screen, WIDTH // 2 - 100, HEIGHT // 2 - 30)  # Draw the "Game Over" message
            if game.score > highest_score:
                Data.push(name=name, score=game.score)
                with open("new_score.txt", "w") as f:
                    f.write(str(game.score))
            # You can add a "Press any key to restart" message here
            if event.type == pygame.KEYDOWN:
                game = Tetris(WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE)
            # Check for the KEYDOWN event
        # Update the display
        pygame.display.flip()
        # Set the framerate
        clock.tick(60)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass