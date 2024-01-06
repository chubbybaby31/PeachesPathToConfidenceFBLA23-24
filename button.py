import pygame, sys
from pygame.locals import *

class Button:
    def __init__(self, font, text, text_color, button_rect, button_color, button_hover_color):
        self.button_rect = button_rect
        self.button_color = button_color
        self.button_hover_color = button_hover_color
        self.text = font.render(text, True, text_color)
        self.text_rect = self.text.get_rect(center=self.button_rect.center)
    
    def draw_button(self, screen, mPos):
        if self.checkHover(mPos):
            pygame.draw.rect(screen, self.button_hover_color, self.button_rect)
        else:
            pygame.draw.rect(screen, self.button_color, self.button_rect)
        screen.blit(self.text, self.text_rect)

    def checkHover(self, mPos):
        return self.button_rect.collidepoint(mPos)