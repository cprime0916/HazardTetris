import sys
import pygame
import random
from tetromino import *
from tetris import Tetris
pygame.init()

# Screen dimensions
# WIDTH, HEIGHT = 250, 500
# GRID_SIZE = 25


def draw_score(screen, score, x, y):
    """Draw the score on the screen"""
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (x, y))


def draw_game_over(screen, x, y):
    """Draw the game over text on the screen"""
    font = pygame.font.Font(None, 48)
    text = font.render("Game Over", True, RED)
    screen.blit(text, (x, y))



def hazards():
    global WIND, SNOWING, TYPHOON, EARTHQUAKE
    randnum = random.randint(1, 2000)
    if randnum <= 1:
        WIND[0] = True
        WIND[1] = random.choice(["Left", "Right"])
    elif randnum <= 2:
        SNOWING[0] = True
    elif randnum <= 3:
        TYPHOON[0] = True
    elif randnum <= 4:
        EARTHQUAKE = True


def main():
    # Initialize pygame
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Tetris')
    # Create a clock object
    clock = pygame.time.Clock()
    # Create a Tetris object
    game = Tetris(WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE)
    keys = pygame.key.get_pressed()
    fall_time = 0
    if DIFFICULTY == "Noob":
        fall_speed = 50
    elif DIFFICULTY == "Easy":
        fall_speed = 35
    elif DIFFICULTY == "Normal":
        fall_speed = 20
    elif DIFFICULTY == "Hard":
        fall_speed = 15
    elif DIFFICULTY == "GLITCH":
        fall_speed = 10
    elif DIFFICULTY == "Asian":
        fall_speed = 3
    else:
      fall_speed = 20  # You can adjust this value to change the falling speed, it's in milliseconds

    while True:
        hazards()
        # is_snowing = snowing()
        # if is_snowing:
        #     game.snow_block()

        # Fill the screen with black
        screen.fill(BLACK)
        for event in pygame.event.get():
            # Check for the QUIT event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Check for the KEYDOWN event
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if game.current_piece.x >= 1:
                        game.current_piece.x -= 1 # Move the piece to the left
                if event.key == pygame.K_RIGHT:
                    if game.valid_move(game.current_piece, 1, 0, 0):
                        game.current_piece.x += 1 # Move the piece to the right
                if event.key == pygame.K_DOWN:
                    if game.valid_move(game.current_piece, 0, 1, 0):
                        game.current_piece.y += 1 # Move the piece down
                if event.key == pygame.K_UP:
                    if game.valid_move(game.current_piece, 0, 0, 1):
                        game.current_piece.rotation += 1 # Rotate the piece
                if event.key == pygame.K_SPACE:
                    while game.valid_move(game.current_piece, 0, 1, 0):
                        game.current_piece.y += 1 # Move the piece down until it hits the bottom
                    game.lock_piece(game.current_piece) # Lock the piece in place
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
        # Draw the grid and the current piece
        game.draw(screen)
        if game.game_over:
            # Draw the "Game Over" message
            draw_game_over(screen, WIDTH // 2 - 100, HEIGHT // 2 - 30)  # Draw the "Game Over" message
            # You can add a "Press any key to restart" message here
            if event.type == pygame.KEYDOWN:
                game = Tetris(WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE)
            # Check for the KEYDOWN event
        # Update the display
        pygame.display.flip()
        # Set the framerate
        clock.tick(60)


if __name__ == "__main__":
    main()