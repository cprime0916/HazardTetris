import pygame
from const import *
class Button:
    def __init__(self, x, y, text):
        self.rect = pygame.Rect(x, y, 800, 600)
        self.text = text
    def draw(self):
        pygame.draw.rect(screen, BLUE, self.rect)
        font = pygame.font.Font(None, 30)
        text = font.render(self.text, True, WHITE)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)