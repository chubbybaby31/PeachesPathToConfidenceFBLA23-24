import pygame
import sys
import math
import time
from movement import Movement
pygame.init()
ms = Movement()


#screen setup
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("")
game_over = False
global back
back = False
global inst
inst = False
global running 
running = True

#background
background= pygame.image.load("bg.png")
menuScreen = pygame.image.load("Aarush/menuScreen.png")
menuScreen = pygame.transform.scale(menuScreen, (900,600))
mapblock1 = pygame.Rect(0, 205, 115, 360)
mapblock2 = pygame.Rect(0, 203, 690, 227)
mapblock3 = pygame.Rect(178, 495, 622, 105)
mapblock4 = pygame.Rect(753, 0, 47, 600)
mapblock5 = pygame.Rect(0, 0, 47, 600)
mapblock6 = pygame.Rect(106, 0, 694, 123)

#character
character_speed = 2
character_size = 50
character = pygame.image.load('pig.png')
character = pygame.transform.scale(character, (50,60))
characterRect = character.get_rect()
characterRect.x = 120
characterRect.y= 550

#levelpads
level1_image = pygame.image.load("level.png")
level1_image = pygame.transform.scale(level1_image, (60,60))
level1 = level1_image.get_rect()
level1.x = 115
level1.y = 440

level2_image = pygame.image.load("level.png")
level2_image = pygame.transform.scale(level2_image, (60,60))
level2 = level2_image.get_rect()
level2.x = 692
level2.y = 220

level3_image = pygame.image.load("level.png")
level3_image = pygame.transform.scale(level3_image, (60,60))
level3 = level3_image.get_rect()
level3.x = 43
level3.y = 87


#only walking on path
def will_collide(rect, dx, dy):
    future_rect = rect.copy() 
    future_rect.move_ip(dx, dy)
    return future_rect.colliderect(mapblock1) or future_rect.colliderect(mapblock2) or future_rect.colliderect(mapblock3) or future_rect.colliderect(mapblock4) or future_rect.colliderect(mapblock5) or future_rect.colliderect(mapblock6)

def wrap_text(message, font, max_width):
    words = message.split(' ')
    lines = []
    current_line = ''

    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line) 
            current_line = word + " "  

    lines.append(current_line)  
    return lines

def display_text_screen(screen, message, typewriter_speed=0.05):
    font = pygame.font.SysFont(None, 50)
    wrapped_text = wrap_text(message, font, screen_width - 60)  
    screen.fill((225,225,225))
    
    y_offset = 0
    for line in wrapped_text:
        for i in range(1, len(line) + 1):
            text = font.render(line[:i], True, (0, 0, 0))
            text_rect = text.get_rect(center=(screen_width // 2, screen_height // 5 + y_offset))
            screen.fill((225,225,225), (0, screen_height // 5 + y_offset - 20, screen_width, 40 + y_offset))  
            screen.blit(text, text_rect)
            pygame.display.flip()
            time.sleep(typewriter_speed)

        y_offset += font.get_height() +5  


def show_popup(screen, message):
    font = pygame.font.SysFont(None, 40)
    text = font.render(message, True, (0, 0, 0))
    text_rect = text.get_rect(center=(screen_width/2, screen_height/2))
    pygame.draw.rect(screen, (255, 255, 255), text_rect.inflate(20, 20))  
    screen.blit(text, text_rect)
    pygame.display.flip()

def dist(X, Y):
    distance = math.sqrt((characterRect.x - X)**2 + (characterRect.y - Y)**2)
    return distance

def levelSel():
    
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

   

    keys = pygame.key.get_pressed()
    if characterRect.colliderect(level1):
        show_popup(screen, "Click Enter to Play")
        if keys[pygame.K_RETURN]:
            display_text_screen(screen, "Level 1: Peaches must gain the confidence to make it out of the farm. Explore through the farm gaining confidence as you go and finding the chests containing 3 keys of confidence to unlock farm exit.")
            time.sleep(1)        
            ms.game()
    if characterRect.colliderect(level2):
        show_popup(screen, "Click Enter to Play")        
        if keys[pygame.K_RETURN]:
            display_text_screen(screen, "Level 2: Peaches is making her way to the mountains where the wolves live but encounters a forest. Make it through the forest and find all 3 chests containing keys to confidence to get to the base of the mountain.")
            time.sleep(1)        
            ms.game()
    if characterRect.colliderect(level3):
        show_popup(screen, "Click Enter to Play")
        if keys[pygame.K_RETURN]:
            display_text_screen(screen, "Level 3: Final stretch. The wolf's den is at the top of a 10,000 feet mountain. Peaches must make it to the top and recover all the stolen food. Navigate through the tough terrain of the mountain and find all three chests containing keys to where the food is hidden.")
            time.sleep(1)        
            ms.game()


def map():
    levelSel()    
    screen.blit(background, (0,0))
    screen.blit(level1_image, level1)
    screen.blit(level2_image, level2)
    screen.blit(level3_image, level3)
    screen.blit(character, characterRect)

def instructions():
    global inst
    screen.fill((225,225,225))    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        inst = False 
    
def winScreen():
    font = pygame.font.Font('Aarush/ARCADE_N.TTF', 60)
    screen.blit(menuScreen, (0,0)) 
    title_text = font.render('LEVEL COMPLETE', True, (0,0,0))
    textRect = title_text.get_rect()
    textRect.center = (screen_width // 2, screen_height // 10)


    
def menu():
    global back
    global inst
    
    if not back and not inst:    
        font = pygame.font.Font('Aarush/ARCADE_N.TTF', 30)
        screen.blit(menuScreen, (0,0)) 
        title_text = font.render('PEACHES PATH TO CONFIDENCE', True, (0,0,0))
        textRect = title_text.get_rect()
        textRect.center = (screen_width // 2, screen_height // 10)
    
                  

        b1_text = font.render('START', True, (0,0,0))
        b1Rect = b1_text.get_rect()
        b1Rect.center = (screen_width // 2, screen_height // 3)

        b2_text = font.render('INSTRUCTIONS', True, (0,0,0))
        b2Rect = b2_text.get_rect()
        b2Rect.center = (screen_width // 2, screen_height // 2)

        b3_text = font.render('QUIT', True, (0,0,0))
        b3Rect = b3_text.get_rect()
        b3Rect.center = (screen_width // 2, screen_height // 1.5)
        
        

        if b1Rect.collidepoint(pygame.mouse.get_pos())== True:
            b1_text = font.render('START', True, (225,0,0))
            
        else:
            b1_text = font.render('START', True, (0,0,0))

        if b2Rect.collidepoint(pygame.mouse.get_pos())== True:
            b2_text = font.render('INSTRUCTIONS', True, (225,0,0))
        else:
            b2_text = font.render('INSTRUCTIONS', True, (0,0,0))

        if b3Rect.collidepoint(pygame.mouse.get_pos())== True:
            b3_text = font.render('QUIT', True, (225,0,0))
        else:
            b3_text = font.render('QUIT', True, (0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and b1Rect.collidepoint(pygame.mouse.get_pos())== True:
                back = True
            elif event.type == pygame.MOUSEBUTTONDOWN and b2Rect.collidepoint(pygame.mouse.get_pos())== True:
                inst = True
            elif event.type == pygame.MOUSEBUTTONDOWN and b3Rect.collidepoint(pygame.mouse.get_pos())== True:
                pygame.quit()
                sys.exit()
    
        screen.blit(title_text, textRect)
        
        pygame.draw.rect(screen, (225,225,225), b1Rect.inflate(20, 20))
        screen.blit(b1_text, b1Rect)
        pygame.draw.rect(screen, (225,225,225), b2Rect.inflate(20, 20))
        screen.blit(b2_text, b2Rect)
        pygame.draw.rect(screen, (225,225,225), b3Rect.inflate(20, 20))
        screen.blit(b3_text, b3Rect)
        pygame.display.flip()
    if back == True:
        map()
    if inst == True:
        instructions()
        
while not game_over:
    keys = pygame.key.get_pressed()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    menu()
    pygame.display.flip()
    

pygame.quit()
