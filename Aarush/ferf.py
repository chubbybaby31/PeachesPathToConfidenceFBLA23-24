import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (255, 255, 255)
BUTTON_COLOR = (100, 100, 100)
HIGHLIGHTED_BUTTON_COLOR = (255, 0, 0)
FONT_SIZE = 40

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Menu Screen with Clickable Buttons")

# Button setup
class Button:
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = BUTTON_COLOR

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.SysFont(None, FONT_SIZE)
        text = font.render(self.text, True, (255, 255, 255))
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def is_hovered_over(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

buttons = [
    Button("Start Game", 300, 200, 200, 50),
    Button("Options", 300, 300, 200, 50),
    Button("Exit", 300, 400, 200, 50)
]

# Game Loop
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                if button.is_hovered_over(mouse_pos):
                    print(f"Clicked on: {button.text}")
                    # Add actions here for each button

    # Render the screen
    screen.fill(BACKGROUND_COLOR)
    for button in buttons:
        button.color = HIGHLIGHTED_BUTTON_COLOR if button.is_hovered_over(mouse_pos) else BUTTON_COLOR
        button.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()