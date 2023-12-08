import pygame
from const import BLUE, WHITE, screen, BUTTON_WIDTH, BUTTON_HEIGHT


class Button:
    def __init__(self, x, y, text):
        self.rect = pygame.Rect(x, y, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.text = text
        self.press_rect = pygame.Rect(0, 0, 0, 0)

    def draw(self):
        pygame.draw.rect(screen, BLUE, self.rect)
        font = pygame.font.Font(None, 30)
        text = font.render(self.text, True, WHITE)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def construct(self, x, y):
        self.press_rect = pygame.Rect(x, y, BUTTON_WIDTH, BUTTON_HEIGHT)

    def on_press(self, event, func, diff, s):
        if self.press_rect.collidepoint(event.pos):
            diff = s
            func(diff)

