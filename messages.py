import pygame, sys
from pygame.locals import *
from button import Button
import world_map
import menu
import level_1, level_2, level_3
import cv2
import numpy as np

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
    cap = cv2.VideoCapture('data/images/storyline.mp4')

    bg_img = pygame.image.load("data/images/storyline.png")
    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

    video_playing = True
    while True:
        clicked = False
        if video_playing:
        # Read a frame from the video
            ret, frame = cap.read()
            if not ret:
                video_playing = False
            else:
                # Convert the frame from BGR to RGB
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.flip(frame, 1)
                # Convert the frame to a Pygame surface
                frame_surface = pygame.surfarray.make_surface(np.rot90(frame))

                # Display the frame on the Pygame window
                screen.blit(frame_surface, (0, 0))
        else:
            # Display the background image
            screen.blit(bg_img, (0, 0))
       
       
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
            play_effect('data/audio/select.wav')
            mode_select()
            pygame.quit()
            sys.exit()

        if clicked and back_button.checkHover(pygame.mouse.get_pos()):
            play_effect('data/audio/select.wav')
            menu.main()
            pygame.quit()
            sys.exit()

        pygame.display.update()
        dt = clock.tick(60)

def mode_select():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('FBLA 2023-24')

    font = pygame.font.Font('data/ARCADE_N.TTF', 20)

    global WINDOW_SIZE
    WINDOW_SIZE = (800, 600)
    cap = cv2.VideoCapture('data/images/mode_select.mp4')

    bg_img = pygame.image.load("data/images/mode_select.png")
    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

    video_playing = True
    while True:
        clicked = False
        if video_playing:
        # Read a frame from the video
            ret, frame = cap.read()
            if not ret:
                video_playing = False
            else:
                # Convert the frame from BGR to RGB
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.flip(frame, 1)
                # Convert the frame to a Pygame surface
                frame_surface = pygame.surfarray.make_surface(np.rot90(frame))

                # Display the frame on the Pygame window
                screen.blit(frame_surface, (0, 0))
        else:
            # Display the background image
            screen.blit(bg_img, (0, 0))
       
       
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                clicked = True
            
        easy_button = Button(font, "EASY", Color("black"), pygame.Rect(WINDOW_SIZE[0] // 2 - 75, 450, 150, 50), Color("white"), Color("gray"))
        easy_button.draw_button(screen, pygame.mouse.get_pos())

        hard_button = Button(font, "HARD", Color("black"), pygame.Rect(WINDOW_SIZE[0] // 2 - 75, 520, 150, 50), Color("white"), Color("gray"))
        hard_button.draw_button(screen, pygame.mouse.get_pos())

        if clicked and easy_button.checkHover(pygame.mouse.get_pos()):
            play_effect('data/audio/select.wav')
            world_map.main(False)

            pygame.quit()
            sys.exit()

        if clicked and hard_button.checkHover(pygame.mouse.get_pos()):
            play_effect('data/audio/select.wav')
            world_map.main(True)
            pygame.quit()
            sys.exit()

        pygame.display.update()
        dt = clock.tick(60)

def level_1_info(difficulty):
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('FBLA 2023-24')

    font = pygame.font.Font('data/ARCADE_N.TTF', 20)

    global WINDOW_SIZE
    WINDOW_SIZE = (800, 600)
    cap = cv2.VideoCapture('data/images/level1.mp4')

    bg_img = pygame.image.load("data/images/level1.png")
    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

    video_playing = True
    while True:
        clicked = False
        if video_playing:
        # Read a frame from the video
            ret, frame = cap.read()
            if not ret:
                video_playing = False
            else:
                # Convert the frame from BGR to RGB
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.flip(frame, 1)
                # Convert the frame to a Pygame surface
                frame_surface = pygame.surfarray.make_surface(np.rot90(frame))

                # Display the frame on the Pygame window
                screen.blit(frame_surface, (0, 0))
        else:
            # Display the background image
            screen.blit(bg_img, (0, 0))
       
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
            play_effect('data/audio/select.wav')
            level_1.main(difficulty)
            pygame.quit()
            sys.exit()

        if clicked and back_button.checkHover(pygame.mouse.get_pos()):
            play_effect('data/audio/select.wav')
            world_map.main(difficulty=difficulty)
            pygame.quit()
            sys.exit()

        pygame.display.update()
        dt = clock.tick(60)

def level_2_info(difficulty, coins):
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('FBLA 2023-24')

    font = pygame.font.Font('data/ARCADE_N.TTF', 20)

    global WINDOW_SIZE
    WINDOW_SIZE = (800, 600)
    cap = cv2.VideoCapture('data/images/level2.mp4')

    bg_img = pygame.image.load("data/images/level2.png")
    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

    video_playing = True
    while True:
        clicked = False
        if video_playing:
        # Read a frame from the video
            ret, frame = cap.read()
            if not ret:
                video_playing = False
            else:
                # Convert the frame from BGR to RGB
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.flip(frame, 1)
                # Convert the frame to a Pygame surface
                frame_surface = pygame.surfarray.make_surface(np.rot90(frame))

                # Display the frame on the Pygame window
                screen.blit(frame_surface, (0, 0))
        else:
            # Display the background image
            screen.blit(bg_img, (0, 0))
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
            play_effect('data/audio/select.wav')
            level_2.main(coins, difficulty=difficulty)
            pygame.quit()
            sys.exit()

        if clicked and back_button.checkHover(pygame.mouse.get_pos()):
            play_effect('data/audio/select.wav')
            world_map.main(difficulty=difficulty, coins=coins)
            pygame.quit()
            sys.exit()

        pygame.display.update()
        dt = clock.tick(60)

def level_3_info(difficulty, coins):
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('FBLA 2023-24')

    font = pygame.font.Font('data/ARCADE_N.TTF', 20)

    global WINDOW_SIZE
    WINDOW_SIZE = (800, 600)
    cap = cv2.VideoCapture('data/images/level3.mp4')

    bg_img = pygame.image.load("data/images/level3.png")
    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

    video_playing = True
    while True:
        clicked = False
        if video_playing:
        # Read a frame from the video
            ret, frame = cap.read()
            if not ret:
                video_playing = False
            else:
                # Convert the frame from BGR to RGB
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.flip(frame, 1)
                # Convert the frame to a Pygame surface
                frame_surface = pygame.surfarray.make_surface(np.rot90(frame))

                # Display the frame on the Pygame window
                screen.blit(frame_surface, (0, 0))
        else:
            # Display the background image
            screen.blit(bg_img, (0, 0))
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
            play_effect('data/audio/select.wav')
            level_3.main(coins, difficulty=difficulty)
            pygame.quit()
            sys.exit()

        if clicked and back_button.checkHover(pygame.mouse.get_pos()):
            play_effect('data/audio/select.wav')
            world_map.main(difficulty=difficulty, coins=coins)
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
            play_effect('data/audio/select.wav')
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
            play_effect('data/audio/select.wav')
            menu.main()
            pygame.quit()
            sys.exit()

        pygame.display.update()
        dt = clock.tick(60)

def shop(coins):
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('FBLA 2023-24')

    font = pygame.font.Font('data/ARCADE_N.TTF', 20)
    global WINDOW_SIZE
    WINDOW_SIZE = (800, 600)

    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
    
    while True:
        clicked = False
        screen.fill(Color("sky blue"))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                clicked = True
            
        back_button = Button(font, "BACK", Color("black"), pygame.Rect(WINDOW_SIZE[0] // 2 - 75, 520, 150, 50), Color("white"), Color("gray"))
        back_button.draw_button(screen, pygame.mouse.get_pos())

        if clicked and back_button.checkHover(pygame.mouse.get_pos()):
            play_effect('data/audio/select.wav')
            world_map.main()
            pygame.quit()
            sys.exit()
        
        coin_text = font.render("COINS: " + str(coins), True, Color("white"))
        coin_text_rect = coin_text.get_rect(center=(100, 30))
        screen.blit(coin_text, coin_text_rect)

        pygame.display.update()
        dt = clock.tick(60)

def play_effect(filename):
    pygame.mixer.Channel(2).play(pygame.mixer.Sound(filename))

if __name__ == '__main__':
    pygame.mixer.init()
    instructions()
