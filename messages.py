import pygame, sys
from pygame.locals import *
from button import Button
import world_map
import menu
import level_1, level_2, level_3

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

def story_line():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('FBLA 2023-24')

    font = pygame.font.Font('data/ARCADE_N.TTF', 20)

    global WINDOW_SIZE
    WINDOW_SIZE = (800, 600)

    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

    message = '''Peaches the pig was leading a contented life on the serene Harmony Farm alongside her fellow animals. One fateful night, a pack of cunning wolves invaded the farm and snatched away the entire food supply. Overwhelmed with fear and lacking confidence, Peaches must now embark on a journy to find the stolen food and gain confidene.'''
    
    while True:
        clicked = False
        screen.fill(Color("sky blue"))
        lines = wrap_text(message, font, WINDOW_SIZE[0] - 20)
        for i, line in enumerate(lines):
            text = font.render(line, True, Color("black"))
            text_rect = text.get_rect(center=(WINDOW_SIZE[0] // 2, 20 + i * 40))
            screen.blit(text, text_rect)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                clicked = True
            
        next_button = Button(font, "NEXT", Color("black"), pygame.Rect(WINDOW_SIZE[0] // 2 - 75, 450, 150, 50), Color("white"), Color("gray"))
        next_button.draw_button(screen, pygame.mouse.get_pos())

        back_button = Button(font, "BACK", Color("black"), pygame.Rect(WINDOW_SIZE[0] // 2 - 75, 520, 150, 50), Color("white"), Color("gray"))
        back_button.draw_button(screen, pygame.mouse.get_pos())

        if clicked and next_button.checkHover(pygame.mouse.get_pos()):
            world_map.main()
            pygame.quit()
            sys.exit()

        if clicked and back_button.checkHover(pygame.mouse.get_pos()):
            menu.main()
            pygame.quit()
            sys.exit()

        pygame.display.update()
        dt = clock.tick(60)

def level_1_info():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('FBLA 2023-24')

    font = pygame.font.Font('data/ARCADE_N.TTF', 20)

    global WINDOW_SIZE
    WINDOW_SIZE = (800, 600)

    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

    message = '''Level 1: Peaches must gain the confidence to make it out of the farm. Explore through the farm gaining confidence as you go and finding the chests containing 3 keys of confidence to unlock the farm exit.'''
    
    while True:
        clicked = False
        screen.fill(Color("sky blue"))
        lines = wrap_text(message, font, WINDOW_SIZE[0] - 20)
        for i, line in enumerate(lines):
            text = font.render(line, True, Color("black"))
            text_rect = text.get_rect(center=(WINDOW_SIZE[0] // 2, 20 + i * 40))
            screen.blit(text, text_rect)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                clicked = True
            
        next_button = Button(font, "NEXT", Color("black"), pygame.Rect(WINDOW_SIZE[0] // 2 - 75, 450, 150, 50), Color("white"), Color("gray"))
        next_button.draw_button(screen, pygame.mouse.get_pos())

        back_button = Button(font, "BACK", Color("black"), pygame.Rect(WINDOW_SIZE[0] // 2 - 75, 520, 150, 50), Color("white"), Color("gray"))
        back_button.draw_button(screen, pygame.mouse.get_pos())

        if clicked and next_button.checkHover(pygame.mouse.get_pos()):
            level_1.main()
            pygame.quit()
            sys.exit()

        if clicked and back_button.checkHover(pygame.mouse.get_pos()):
            world_map.main()
            pygame.quit()
            sys.exit()

        pygame.display.update()
        dt = clock.tick(60)

def level_2_info():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('FBLA 2023-24')

    font = pygame.font.Font('data/ARCADE_N.TTF', 20)

    global WINDOW_SIZE
    WINDOW_SIZE = (800, 600)

    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

    message = '''Level 2: Peaches is making her way to the mountains where the wolves live but encounters a forest. Make it through the forest and find all 3 chests containing keys to confidence to get to the base of the mountain.'''
    
    while True:
        clicked = False
        screen.fill(Color("sky blue"))
        lines = wrap_text(message, font, WINDOW_SIZE[0] - 20)
        for i, line in enumerate(lines):
            text = font.render(line, True, Color("black"))
            text_rect = text.get_rect(center=(WINDOW_SIZE[0] // 2, 20 + i * 40))
            screen.blit(text, text_rect)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                clicked = True
            
        next_button = Button(font, "NEXT", Color("black"), pygame.Rect(WINDOW_SIZE[0] // 2 - 75, 450, 150, 50), Color("white"), Color("gray"))
        next_button.draw_button(screen, pygame.mouse.get_pos())

        back_button = Button(font, "BACK", Color("black"), pygame.Rect(WINDOW_SIZE[0] // 2 - 75, 520, 150, 50), Color("white"), Color("gray"))
        back_button.draw_button(screen, pygame.mouse.get_pos())

        if clicked and next_button.checkHover(pygame.mouse.get_pos()):
            level_2.main()
            pygame.quit()
            sys.exit()

        if clicked and back_button.checkHover(pygame.mouse.get_pos()):
            world_map.main()
            pygame.quit()
            sys.exit()

        pygame.display.update()
        dt = clock.tick(60)

def level_3_info():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('FBLA 2023-24')

    font = pygame.font.Font('data/ARCADE_N.TTF', 20)

    global WINDOW_SIZE
    WINDOW_SIZE = (800, 600)

    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

    message = '''Level 3: Final stretch. The wolf's den is at the top of a 10,000 feet mountain. Peaches must make it to the top and recover all the stolen food. Navigate through the tough terrain of the mountain and find all three chests containing keys to confidence. Then you must fine where the food is hidden.'''
    
    while True:
        clicked = False
        screen.fill(Color("sky blue"))
        lines = wrap_text(message, font, WINDOW_SIZE[0] - 20)
        for i, line in enumerate(lines):
            text = font.render(line, True, Color("black"))
            text_rect = text.get_rect(center=(WINDOW_SIZE[0] // 2, 20 + i * 40))
            screen.blit(text, text_rect)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                clicked = True
            
        next_button = Button(font, "NEXT", Color("black"), pygame.Rect(WINDOW_SIZE[0] // 2 - 75, 450, 150, 50), Color("white"), Color("gray"))
        next_button.draw_button(screen, pygame.mouse.get_pos())

        back_button = Button(font, "BACK", Color("black"), pygame.Rect(WINDOW_SIZE[0] // 2 - 75, 520, 150, 50), Color("white"), Color("gray"))
        back_button.draw_button(screen, pygame.mouse.get_pos())

        if clicked and next_button.checkHover(pygame.mouse.get_pos()):
            level_3.main()
            pygame.quit()
            sys.exit()

        if clicked and back_button.checkHover(pygame.mouse.get_pos()):
            world_map.main()
            pygame.quit()
            sys.exit()

        pygame.display.update()
        dt = clock.tick(60)

def instructions():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('FBLA 2023-24')

    font = pygame.font.Font('data/ARCADE_N.TTF', 20)

    global WINDOW_SIZE
    WINDOW_SIZE = (800, 600)

    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

    message = '''Take on the role as Peaches, an unconfident pig who has embarked on a journey to find her missing food. In each level, you will need to navigate through the map, with the arrow keys, and unlock chests that hold the secrete to confidence. Once all chests are unlocked in a level, you can exit the map by exiting through a door. But be careful. There are several wolves placed around the map to prevent you from succeeding. Goodluck on your journy!'''
    
    while True:
        clicked = False
        screen.fill(Color("sky blue"))
        lines = wrap_text(message, font, WINDOW_SIZE[0] - 20)
        for i, line in enumerate(lines):
            text = font.render(line, True, Color("black"))
            text_rect = text.get_rect(center=(WINDOW_SIZE[0] // 2, 20 + i * 40))
            screen.blit(text, text_rect)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                clicked = True

        back_button = Button(font, "BACK", Color("black"), pygame.Rect(WINDOW_SIZE[0] // 2 - 75, 520, 150, 50), Color("white"), Color("gray"))
        back_button.draw_button(screen, pygame.mouse.get_pos())

        if clicked and back_button.checkHover(pygame.mouse.get_pos()):
            menu.main()
            pygame.quit()
            sys.exit()

        pygame.display.update()
        dt = clock.tick(60)

def final():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('FBLA 2023-24')

    font = pygame.font.Font('data/ARCADE_N.TTF', 20)
    global WINDOW_SIZE
    WINDOW_SIZE = (800, 600)

    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

    message = '''Triumphant, Peaches returns to Harmony Farm with the food, earning the respect and admiration of all the animals. She realizes that her courage was always present, just waiting to be discovered'''
    
    while True:
        clicked = False
        screen.fill(Color("sky blue"))
        lines = wrap_text(message, font, WINDOW_SIZE[0] - 20)
        for i, line in enumerate(lines):
            text = font.render(line, True, Color("black"))
            text_rect = text.get_rect(center=(WINDOW_SIZE[0] // 2, 20 + i * 40))
            screen.blit(text, text_rect)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                clicked = True
            
        next_button = Button(font, "QUIT", Color("black"), pygame.Rect(WINDOW_SIZE[0] // 2 - 75, 450, 150, 50), Color("white"), Color("gray"))
        next_button.draw_button(screen, pygame.mouse.get_pos())

        back_button = Button(font, "MENU", Color("black"), pygame.Rect(WINDOW_SIZE[0] // 2 - 75, 520, 150, 50), Color("white"), Color("gray"))
        back_button.draw_button(screen, pygame.mouse.get_pos())

        if clicked and next_button.checkHover(pygame.mouse.get_pos()):
            pygame.quit()
            sys.exit()

        if clicked and back_button.checkHover(pygame.mouse.get_pos()):
            menu.main()
            pygame.quit()
            sys.exit()

        pygame.display.update()
        dt = clock.tick(60)

if __name__ == '__main__':
    instructions()