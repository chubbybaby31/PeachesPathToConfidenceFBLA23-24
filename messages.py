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
        dt = clock.tick(30)

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
        dt = clock.tick(30)

def level_1_info(difficulty, power_ups):
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
            level_1.main(power_ups, difficulty=difficulty)
            pygame.quit()
            sys.exit()

        if clicked and back_button.checkHover(pygame.mouse.get_pos()):
            play_effect('data/audio/select.wav')
            world_map.main(difficulty=difficulty, level=1, power_ups=power_ups)
            pygame.quit()
            sys.exit()

        pygame.display.update()
        dt = clock.tick(30)

def level_2_info(difficulty, coins, power_ups):
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
            level_2.main(coins, power_ups, difficulty=difficulty)
            pygame.quit()
            sys.exit()

        if clicked and back_button.checkHover(pygame.mouse.get_pos()):
            play_effect('data/audio/select.wav')
            world_map.main(difficulty=difficulty, coins=coins, level=2, power_ups=power_ups)
            pygame.quit()
            sys.exit()

        pygame.display.update()
        dt = clock.tick(30)

def level_3_info(difficulty, coins, power_ups):
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
            level_3.main(coins, power_ups, difficulty=difficulty)
            pygame.quit()
            sys.exit()

        if clicked and back_button.checkHover(pygame.mouse.get_pos()):
            play_effect('data/audio/select.wav')
            world_map.main(difficulty=difficulty, coins=coins, level=3, power_ups=power_ups)
            pygame.quit()
            sys.exit()

        pygame.display.update()
        dt = clock.tick(30)

def instructions1():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('FBLA 2023-24')

    font = pygame.font.Font('data/ARCADE_N.TTF', 20)
    bg_img = pygame.image.load("data/images/instructions1.png")

    global WINDOW_SIZE
    WINDOW_SIZE = (800, 600)

    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

    while True:
        clicked = False
        screen.blit(bg_img, (0, 0))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                clicked = True

        controls_button = Button(font, "CONTROLS", Color("black"), pygame.Rect(WINDOW_SIZE[0] // 2 - 87.5, 520, 175, 50), Color("white"), Color("gray"))
        controls_button.draw_button(screen, pygame.mouse.get_pos())

        if clicked and controls_button.checkHover(pygame.mouse.get_pos()):
            play_effect('data/audio/select.wav')
            instructions2()
            
        pygame.display.update()
        dt = clock.tick(60)

def instructions2():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('FBLA 2023-24')

    font = pygame.font.Font('data/ARCADE_N.TTF', 20)
    bg_img = pygame.image.load("data/images/instructions2.png")
    

    global WINDOW_SIZE
    WINDOW_SIZE = (800, 600)

    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
    
    while True:
        clicked = False
        screen.blit(bg_img, (0, 0))
        
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
    bg_img = pygame.image.load("data/images/endscreen.png")

    while True:
        clicked = False
        screen.blit(bg_img, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                clicked = True
            
        next_button = Button(font, "QUIT", Color("black"), pygame.Rect(WINDOW_SIZE[0] // 2 - 75, 75, 150, 50), Color("white"), Color("gray"))
        next_button.draw_button(screen, pygame.mouse.get_pos())

        back_button = Button(font, "MENU", Color("black"), pygame.Rect(WINDOW_SIZE[0] // 2 - 75, 150, 150, 50), Color("white"), Color("gray"))
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

def shop(coins, level, power_ups):
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('FBLA 2023-24')

    dash_board = False
    doublejump_board = False
    extralife_board = False

    prices = {"double jump": "$20", "extra life": "$20", "dash": "$20"}
    if power_ups[0]: prices["double jump"] = "SOLD"
    if power_ups[1]: prices["extra life"] = "SOLD"
    if power_ups[2]: prices["dash"] = "SOLD"

    font = pygame.font.Font('data/ARCADE_N.TTF', 20)

    global WINDOW_SIZE
    WINDOW_SIZE = (800, 600)
    cap = cv2.VideoCapture('data/images/shop.mp4')

    bg_img = pygame.image.load("data/images/shop.png")
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
            
        back_button = Button(font, "BACK", Color("black"), pygame.Rect(WINDOW_SIZE[0] // 2 - 75, 520, 150, 50), Color("white"), Color("gray"))
        back_button.draw_button(screen, pygame.mouse.get_pos())

        doublejump_button = pygame.image.load('data/images/doublejump.png')  
        doublejump_button = pygame.transform.scale(doublejump_button, (100, 75))
        doublejump_button_rect = doublejump_button.get_rect()
        doublejump_button_rect.topleft = (200 , 280)

        extralife_button = pygame.image.load('data/images/extralife.png')  
        extralife_button = pygame.transform.scale(extralife_button, (100, 75))
        extralife_button_rect = extralife_button.get_rect()
        extralife_button_rect.topleft = (60 , 280)

        dash_button = pygame.image.load('data/images/dash.png')  
        dash_button = pygame.transform.scale(dash_button, (100, 75))
        dash_button_rect = dash_button.get_rect()
        dash_button_rect.topleft = (350 , 280)

        doublejumpboard = pygame.image.load('data/images/doublejumpboard.png')  
        doublejumpboard_rect = doublejumpboard.get_rect()
        doublejumpboard_rect.topleft = (30 , -20)

        dashboard = pygame.image.load('data/images/dashboard.png')  
        dashboard_rect = dashboard.get_rect()
        dashboard_rect.topleft = (30 , -20)

        extralifeboard = pygame.image.load('data/images/extralifeboard.png')  
        extralifeboard_rect = extralifeboard.get_rect()
        extralifeboard_rect.topleft = (30 , -20)
        
        buydash_button = Button(font, prices["dash"], Color("black"), pygame.Rect(600, 435, 150, 50), Color("light green"), Color("gray"))

        buydoublejump_button = Button(font, prices["double jump"], Color("black"), pygame.Rect(600, 435, 150, 50), Color("light green"), Color("gray"))

        buyextralife_button = Button(font, prices["extra life"], Color("black"), pygame.Rect(600, 435, 150, 50), Color("light green"), Color("gray"))

        if clicked and back_button.checkHover(pygame.mouse.get_pos()):
            play_effect('data/audio/select.wav')
            world_map.main(coins=coins, level=level, power_ups=power_ups)
            pygame.quit()
            sys.exit()

        if doublejump_button_rect.collidepoint(pygame.mouse.get_pos()):
            doublejump_button = pygame.transform.scale(doublejump_button, (110, 83))
            doublejump_button_rect.topleft = (195 , 276)
            if clicked:
                play_effect('data/audio/select.wav')
                dash_board = False
                doublejump_board = True
                extralife_board = False
            

        if extralife_button_rect.collidepoint(pygame.mouse.get_pos()):
            extralife_button = pygame.transform.scale(extralife_button, (110, 83))
            extralife_button_rect.topleft = (55 , 276)
            if clicked:
                play_effect('data/audio/select.wav')
                dash_board = False
                doublejump_board = False
                extralife_board = True

        if dash_button_rect.collidepoint(pygame.mouse.get_pos()):
            dash_button = pygame.transform.scale(dash_button, (110, 83))
            dash_button_rect.topleft = (345 , 276)
            if clicked:
                play_effect('data/audio/select.wav')
                dash_board = True
                doublejump_board = False
                extralife_board = False

        if dash_board:
            screen.blit(dashboard, dashboard_rect.topleft)
            if clicked and buydash_button.checkHover(pygame.mouse.get_pos()):
                if coins >= 20 and not power_ups[2]:
                    play_effect('data/audio/buy.wav')
                    power_ups[2] = True
                    prices["dash"] = "SOLD"
                    coins -= 20
                    buydash_button = Button(font, "SOLD", Color("black"), pygame.Rect(600, 435, 150, 50), Color("light green"), Color("gray"))
                else: play_effect('data/audio/sold.wav')
            buydash_button.draw_button(screen, pygame.mouse.get_pos())

        if extralife_board:
            screen.blit(extralifeboard, extralifeboard_rect.topleft)
            if clicked and buyextralife_button.checkHover(pygame.mouse.get_pos()):
                if coins >= 20 and not power_ups[1]:
                    play_effect('data/audio/buy.wav')
                    power_ups[1] = True
                    prices["extra life"] = "SOLD"
                    coins -= 20
                    buyextralife_button = Button(font, "SOLD", Color("black"), pygame.Rect(600, 435, 150, 50), Color("light green"), Color("gray"))
                else: play_effect('data/audio/sold.wav')
            buyextralife_button.draw_button(screen, pygame.mouse.get_pos())

        if doublejump_board:
            screen.blit(doublejumpboard, doublejumpboard_rect.topleft)
            if clicked and buydoublejump_button.checkHover(pygame.mouse.get_pos()):
                if coins >= 20 and not power_ups[0]:
                    play_effect('data/audio/buy.wav')
                    power_ups[0] = True
                    prices["double jump"] = "SOLD"
                    coins -= 20
                    buydoublejump_button = Button(font, "SOLD", Color("black"), pygame.Rect(600, 435, 150, 50), Color("light green"), Color("gray"))
                else: play_effect('data/audio/sold.wav')
            buydoublejump_button.draw_button(screen, pygame.mouse.get_pos())
        
        coin_text = font.render("COINS: " + str(coins), True, Color("black"))
        coin_text_rect = coin_text.get_rect(center=(100, 30))
        screen.blit(coin_text, coin_text_rect)
        screen.blit(doublejump_button, doublejump_button_rect.topleft)
        screen.blit(extralife_button, extralife_button_rect.topleft)
        screen.blit(dash_button, dash_button_rect.topleft)

        pygame.display.update()
        dt = clock.tick(30)

def play_effect(filename):
    pygame.mixer.Channel(2).play(pygame.mixer.Sound(filename))

if __name__ == '__main__':
    pygame.mixer.init()
    final()
