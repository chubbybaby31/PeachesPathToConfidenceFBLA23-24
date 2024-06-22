import pygame, sys
from pygame.locals import *
from button import Button
import level_1, level_2, level_3
import messages

def show_popup(screen, message, popup=False):
    font = pygame.font.SysFont(None, 40)
    text = font.render(message, True, (0, 0, 0))
    if popup:
        text_rect = text.get_rect(center=(WINDOW_SIZE[0]/2, WINDOW_SIZE[1] * 7 / 8))
    else: text_rect = text.get_rect(center=(WINDOW_SIZE[0]/2, WINDOW_SIZE[1] / 2))
    pygame.draw.rect(screen, (255, 255, 255), text_rect.inflate(2, 2), border_radius=5)  
    screen.blit(text, text_rect)

def handle_collisions(p_rect, rects, right, left, up, down):
    for rect in rects:
        if rect.colliderect(p_rect):
            if right:
                p_rect.right = rect.left
            elif left:
                p_rect.left = rect.right
            elif up:
                p_rect.top = rect.bottom
            elif down:
                p_rect.bottom = rect.top        
    return p_rect

def main(difficulty=False, coins=0, level=0):
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('FBLA 2023-24')

    global WINDOW_SIZE
    WINDOW_SIZE = (800, 600)

    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
    bg_img = pygame.image.load("data/images/map_bg.png")
    bg_img = pygame.transform.scale(bg_img, WINDOW_SIZE)


    border_rects = [pygame.Rect(176, 488, 623, 111),
                    pygame.Rect(608, 182, 84, 250),
                    pygame.Rect(0, 200, 609, 230),
                    pygame.Rect(0, 0, 44, 207),
                    pygame.Rect(103, 0, 696, 124),
                    pygame.Rect(103, 0, 445, 143),
                    pygame.Rect(356, 143, 192, 15),
                    pygame.Rect(0, 428, 116, 171),
                    pygame.Rect(752, 120, 47, 479)]

    player_img = pygame.image.load("data/images/entities/player/idle/idle_0.png")
    player_img = pygame.transform.scale(player_img, (24, 30))
    player_rect = player_img.get_rect()
    level_pos = {0: [134, 569], 1: [145, 460], 2: [720, 150]}
    player_pos = level_pos[level]
    player_speed = 4

    level_select_img = pygame.image.load("data/images/level.png")
    level_select_img = pygame.transform.scale(level_select_img, (40, 40))

    level_1_select = level_select_img.get_rect(center=(145, 460))
    level_2_select = level_select_img.get_rect(center=(720, 150))
    level_3_select = level_select_img.get_rect(center=(70, 90))

    level_rects = [level_1_select, level_2_select, level_3_select]
    
    move_left = False
    move_right = False
    move_up = False
    move_down = False

    game_font = pygame.font.Font('data/ARCADE_N.TTF', 25)
    while True:
        clicked=False
        collision_levels = [False, False, False]
        screen.blit(bg_img, (0, 0))

        for rect in level_rects:
            screen.blit(level_select_img, rect)

        player_rect.x = player_pos[0]
        player_rect.y = player_pos[1]
        screen.blit(player_img, (player_pos[0], player_pos[1]))
        
        font = pygame.font.Font('data/ARCADE_N.TTF', 20)

        shop_button = Button(font, "SHOP", Color("black"), pygame.Rect(WINDOW_SIZE[0] - 175, 10, 150, 50), Color("white"), Color("gray"))
        shop_button.draw_button(screen, pygame.mouse.get_pos())

        if level_1_select.colliderect(player_rect):
            show_popup(screen, "PRESS ENTER TO START")
            collision_levels[0] = True
        elif level_2_select.colliderect(player_rect):
            show_popup(screen, "PRESS ENTER TO START")
            collision_levels[1] = True
        elif level_3_select.colliderect(player_rect):
            show_popup(screen, "PRESS ENTER TO START")
            collision_levels[2] = True

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                clicked = True
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    move_right = True
                    move_left = False
                    move_up = False
                    move_down = False
                if event.key == K_LEFT:
                    move_right = False
                    move_left = True
                    move_up = False
                    move_down = False
                if event.key == K_UP:
                    move_right = False
                    move_left = False
                    move_up = True
                    move_down = False
                if event.key == K_DOWN:
                    move_right = False
                    move_left = False
                    move_up = False
                    move_down = True
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    move_right = False
                if event.key == K_LEFT:
                    move_left = False
                if event.key == K_UP:
                    move_up = False
                if event.key == K_DOWN:
                    move_down = False
                
                if event.key == K_RETURN:
                    if collision_levels[0]:
                        play_effect('data/audio/enterlevel.wav')
                        messages.level_1_info(difficulty)
                        pygame.quit()
                        sys.exit()
                    elif collision_levels[1]:
                        play_effect('data/audio/enterlevel.wav')

                        messages.level_2_info(difficulty, coins)
                        pygame.quit()
                        sys.exit()
                    elif collision_levels[2]:
                        play_effect('data/audio/enterlevel.wav')
                        messages.level_3_info(difficulty, coins)
                        pygame.quit()
                        sys.exit()
        if move_right:
            player_rect.x += player_speed
        elif move_left:
            player_rect.x -= player_speed
        elif move_up:
            player_rect.y -= player_speed
        elif move_down:
            player_rect.y += player_speed

        if shop_button.checkHover(pygame.mouse.get_pos()):
            if clicked and not difficulty:
                play_effect('data/audio/select.wav')
                messages.shop(coins)
            elif difficulty:
                show_popup(screen, "CAN'T USE SHOP IN HARD MODE")

        player_rect = handle_collisions(player_rect, border_rects, move_right, move_left, move_up, move_down)
        player_pos = [player_rect.x, player_rect.y]

        coin_text = game_font.render("COINS: " + str(coins), True, Color("white"))
        coin_text_rect = coin_text.get_rect(center=(120, 30))
        screen.blit(coin_text, coin_text_rect)
            
        pygame.display.update()
        pygame.display.flip()
        dt = clock.tick(60)

def play_effect(filename):
    pygame.mixer.Channel(3).play(pygame.mixer.Sound(filename))

if __name__ == '__main__':
    pygame.mixer.init()
    main()
