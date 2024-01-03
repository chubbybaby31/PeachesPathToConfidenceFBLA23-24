import pygame
import sys
import math

pygame.init()
#screen setup
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("")
game_over = False
current_frame = 0
frame_rate = 10 


#background
background= pygame.image.load("bg.png")
mapblock1 = pygame.Rect(0, 205, 115, 360)
mapblock2 = pygame.Rect(0, 203, 690, 227)
mapblock3 = pygame.Rect(178, 495, 622, 105)
mapblock4 = pygame.Rect(753, 0, 47, 600)
mapblock5 = pygame.Rect(0, 0, 47, 600)
mapblock6 = pygame.Rect(106, 0, 694, 123)

#character
character_speed = 2
character_size = 50
character = pygame.image.load('1.png')
character = pygame.transform.scale(character, (50,60))
characterRect = character.get_rect()
characterRect.x = 120
characterRect.y= 550

#levelpads
Level1 = pygame.image.load("level.png")
Level1 = pygame.transform.scale(Level1, (60,60))
level1 = Level1.get_rect()
level1.x = 115
level1.y = 440

Level2 = pygame.image.load("level.png")
Level2 = pygame.transform.scale(Level2, (60,60))
level2 = Level2.get_rect()
level2.x = 692
level2.y = 220

Level3 = pygame.image.load("level.png")
Level3 = pygame.transform.scale(Level3, (60,60))
level3 = Level3.get_rect()
level3.x = 43
level3.y = 87


#only walking on path
def will_collide(rect, dx, dy):
    future_rect = rect.copy() 
    future_rect.move_ip(dx, dy)
    return future_rect.colliderect(mapblock1) or future_rect.colliderect(mapblock2) or future_rect.colliderect(mapblock3) or future_rect.colliderect(mapblock4) or future_rect.colliderect(mapblock5) or future_rect.colliderect(mapblock6)

def charMove():
    print(characterRect.x, characterRect.y)
    keys = pygame.key.get_pressed()
    dx = dy = 0
    if keys[pygame.K_LEFT]:
        dx = -character_speed
    if keys[pygame.K_RIGHT]:
        dx = character_speed
    if keys[pygame.K_UP]:
        dy = -character_speed
    if keys[pygame.K_DOWN]:
        dy = character_speed

    if not will_collide(characterRect, dx, 0):
        characterRect.x = max(0, min(screen_width - character_size, characterRect.x + dx))
    if not will_collide(characterRect, 0, dy):
        characterRect.y = max(0, min(screen_height - character_size, characterRect.y + dy))


def show_popup(screen, message):
    font = pygame.font.SysFont(None, 40)
    text = font.render(message, True, (0, 0, 0))
    text_rect = text.get_rect(center=(screen_width/2, screen_height/2))
    pygame.draw.rect(screen, (255, 255, 255), text_rect.inflate(20, 20))  
    screen.blit(text, text_rect)
    pygame.display.flip()


def dist( X, Y):
    distance = math.sqrt((characterRect.x - X)**2 + (characterRect.y - Y)**2)
    return distance

def levelSel():
    if characterRect.colliderect(level1) or dist(level1.x, level1.y)< 30:
        show_popup(screen, "Click Enter to Play")

    if characterRect.colliderect(level2):
        show_popup(screen, "Click Enter to Play")        

    if characterRect.colliderect(level3):
        show_popup(screen, "Click Enter to Play")



while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
   
    charMove()
    levelSel()

    
  

    screen.blit(background, (0,0))
    screen.blit(Level1, level1)
    screen.blit(Level2, level2)
    screen.blit(Level3, level3)
    screen.blit(character, characterRect)

    pygame.display.flip()
    

pygame.quit()