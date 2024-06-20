import pygame, sys, math
import data.engine as e
from pygame.locals import *
from button import Button
import menu
import world_map
from _thread import start_new_thread
from mouse import Mouse

global musicCounter
musicCounter = 0
hand = Mouse()

def load_map(path):
    f = open(path + '.txt', 'r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))
    return game_map

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

def show_popup(screen, message, popup=False):
    font = pygame.font.Font('data/ARCADE_N.TTF', 10)
    lines = wrap_text(message, font, DISPLAY_SIZE[0] - 50)
    for i, t in enumerate(lines):
        text = font.render(t, True, (0, 0, 0))
        if popup:
            text_rect = text.get_rect(center=(DISPLAY_SIZE[0]/2, DISPLAY_SIZE[1] * 7 / 8))
        else: text_rect = text.get_rect(center=(DISPLAY_SIZE[0]/2, 100 + 10 * i))
        pygame.draw.rect(screen, (255, 255, 255), text_rect.inflate(2, 2), border_radius=5)  
        screen.blit(text, text_rect)

def main(difficulty=False):
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('FBLA 2023-24')

    global WINDOW_SIZE
    WINDOW_SIZE = (800, 600)

    global DISPLAY_SIZE
    DISPLAY_SIZE = (400, 300)
    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
    display = pygame.Surface(DISPLAY_SIZE)
    end_game_screen = pygame.Surface(WINDOW_SIZE)

    e.load_animations('data/images/entities/')

    game_map = load_map('map_1')

    grass_image = pygame.image.load('data/images/grass.png')
    dirt_image = pygame.image.load('data/images/dirt.png')
    chest_image = pygame.image.load('data/images/chest.png')
    door_image = pygame.image.load('data/images/door_closed.png')
    farm_image = pygame.image.load('data/images/farm.png')
    coin_image = pygame.image.load('data/images/coin_angle.png')
    TILE_SIZE = dirt_image.get_width()

    GUI_font = pygame.font.Font('data/ARCADE_N.TTF', 10)
    EG_font = pygame.font.Font('data/ARCADE_N.TTF', 25)

    confidence_quips = {3: "Set Small Goals: Start with achievable goals to build up your sense of accomplishment. Completing small tasks successfully can boost your confidence gradually.", 
                        4: "Positive Self-Talk: Replace negative thoughts with positive affirmations. Remind yourself of your strengths and achievements, no matter how small they may seem.", 
                        5: "Learn New Skills: Acquiring new skills or hobbies can enhance your self-esteem. It shows you are capable of growth and adaptability."}

    confidence_collected = {3: False, 4: False, 5: False}

    c_pts = 0
    max_c_pts = 3

    moving_right = False
    moving_left = False

    player_y_momentum = 0
    air_timer = 0

    true_scroll = [0, 0]

    player = e.entity(0, 400, 20, 25, 'player')

    enemies = []
    enemies.append([2, 0, e.entity(550, 330, 28, 20, 'enemy')])
    enemies.append([2, 0, e.entity(900, 540, 28, 20, 'enemy')])
    enemies.append([2, 0, e.entity(1000, 200, 28, 20, 'enemy')])
    enemies.append([2, 0, e.entity(1100, 200, 28, 20, 'enemy')])
    enemies.append([2, 0, e.entity(350, 90, 28, 20, 'enemy')])
    enemies.append([2, 0, e.entity(300, 140, 28, 20, 'enemy')])
    enemies.append([2, 0, e.entity(400, 140, 28, 20, 'enemy')])

    near_chest = False
    current_chest_id = None

    near_door = False

    lives = 20
    invincible = False
    invincible_timer = 0
    game_over = False
    handMove = False
    coins_collected = 0
    coins_collected_pos = []
    while True:
        clicked = False

        if player.y >= 600:
            lives = 0
        
        if lives <= 0:
            game_over = True

        chest_popup_id = None

        display.fill(Color("sky blue"))

        true_scroll[0] += (player.x - true_scroll[0] - 152) / 20
        true_scroll[1] += (player.y - true_scroll[1] - 106) / 20
        scroll = true_scroll.copy()
        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])

        display.blit(pygame.transform.scale(farm_image, (120, 120)), (DISPLAY_SIZE[0] // 2 - 60, 17))
        pygame.draw.rect(display, (55, 148, 86), pygame.Rect(0, 132, 400, 200))

        tile_rects = []
        chests = []
        chest_ids = []
        enemy_borders = []
        coins = []
        for y, row in enumerate(game_map):
            for x, tile in enumerate(row):
                if tile == '*' or tile == 'd' or tile == 'g': 
                    enemy_borders.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                if tile == '1' or tile == 'd':
                    display.blit(dirt_image, (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))
                elif tile == '2' or tile == 'g':
                    display.blit(grass_image, (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))
                elif tile == '8':
                    collected = False
                    for c in coins_collected_pos:
                        if c[0] == x * TILE_SIZE and c[1] == y * TILE_SIZE:
                            collected = True
                            break
                    if not collected:
                        display.blit(coin_image, (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))
                        coins.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                elif tile == '9':
                    display.blit(door_image, (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))
                    door_rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE * 2)
                elif tile == '*': pass
                elif int(tile) > 2:
                    display.blit(chest_image, (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))
                    chests.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                    chest_ids.append(int(tile))
                if tile == '1' or tile == '2' or tile == '9' or tile == 'd' or tile == 'g':
                    tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

        player_movement = [0, 0]
        if moving_right:
            player_movement[0] += 2
        if moving_left:
            player_movement[0] -= 2
        player_movement[1] += player_y_momentum
        player_y_momentum += 0.2
        if player_y_momentum > 3: player_y_momentum = 3

        if player_movement[0] > 0:
            player.set_action('run')
            player.set_flip(False)
        elif player_movement[0] < 0:
            player.set_action('run')
            player.set_flip(True)
        elif player_movement[0] == 0:
            player.set_action('idle')

        collision_types = player.move(player_movement, tile_rects)

        if collision_types['bottom']: 
            player_y_momentum = 0
            air_timer = 0
        else: air_timer += 1

        if collision_types['top']:
            player_y_momentum = 0

        if air_timer > 10:
            player.set_action('idle')

        player.change_frame(1)
        player.display(display, scroll)

        for id, chest in zip(chest_ids, chests):
            distance = math.sqrt((player.x - chest.x)**2 + (player.y - chest.y)**2)
            if distance <= 30 and not near_chest and not confidence_collected[id]:
                chest_popup_id = id
        
        unlocked = True
        for id in chest_ids:
            if not confidence_collected[id]:
                unlocked = False
                break

        if unlocked: door_image = pygame.image.load('data/images/door_opened.png')

        for enemy in enemies:
            enemy[2].set_action('run')
            enemy[1] += 0.2
            enemy_movement = [enemy[0], enemy[1]]
            if enemy[1] > 3: enemy[1] = 3
            collision_types = enemy[2].move(enemy_movement, tile_rects)
            if collision_types['right'] or collision_types['left']: enemy[0] *= -1
            for border in enemy_borders:
                if enemy[2].obj.rect.colliderect(border): 
                    enemy[0] *= -1
                    break
            if enemy[0] < 0: enemy[2].set_flip(True)
            else: enemy[2].set_flip(False)
            if collision_types['bottom'] == True:
                enemy[1] = 0

            enemy[2].display(display, scroll)
            enemy[2].change_frame(1)

            if player.obj.rect.colliderect(enemy[2].obj.rect) and not invincible: 
                play_effect('data/audio/damaged.wav')
                lives -= 1
                invincible = True

        if invincible:
            invincible_timer += dt
        if invincible_timer >= 3000:
            invincible_timer = 0
            invincible = False
        
        for coin in coins:
            if player.obj.rect.colliderect(coin):
                play_effect('data/audio/coin.wav')
                coins_collected_pos.append((coin.x, coin.y))
                coins_collected += 1

        door_distance = math.sqrt((player.x - door_rect.x)**2 + (player.y - door_rect.y)**2)
        if door_distance <= 30 and not near_door and not unlocked:
            show_popup(display, " Unlock all" + str(max_c_pts) + " chests to open door", popup=True)
        elif door_distance <= 30: 
            show_popup(display, " Press ENTER to complete level", popup=True)

        if chest_popup_id != None and not confidence_collected[chest_popup_id]:
            show_popup(display, " Press E to open chest", popup=True)
        elif current_chest_id != None:
            show_popup(display, confidence_quips[current_chest_id])
            show_popup(display, " Press ESC to exit", popup=True)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and not difficulty:
                if event.key == K_RIGHT and current_chest_id == None :
                    moving_right = True
                    handMove = False
                if event.key == K_LEFT and current_chest_id == None:
                    moving_left = True
                    handMove = False
                if event.key == K_UP:
                    handMove = False
                    if air_timer < 6:
                        player_y_momentum = -5
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    moving_right = False
                if event.key == K_LEFT:
                    moving_left = False
                if event.key == K_e and chest_popup_id != None:
                    play_effect('data/audio/chest.wav')
                    confidence_collected[chest_popup_id] = True
                    current_chest_id = chest_popup_id
                    c_pts += 1
                if event.key == K_ESCAPE:
                    current_chest_id = None
                if event.key == K_RETURN and unlocked:
                    play_effect('data/audio/level_complete.wav')
                    print("level complete")
                    game_over = True
            if event.type == MOUSEBUTTONUP:
                clicked = True

        screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0, 0))

        c_pts_text = GUI_font.render("CONFIDENCE POINTS: " + str(c_pts) + "/" + str(max_c_pts), True, Color("white"))
        c_pts_text_rect = c_pts_text.get_rect(center=(120, 12))
        screen.blit(c_pts_text, c_pts_text_rect)

        coin_text = GUI_font.render("COINS: " + str(coins_collected), True, Color("white"))
        coin_text_rect = coin_text.get_rect(center=(51, 30))
        screen.blit(coin_text, coin_text_rect)

        lives_text = GUI_font.render("LIVES: " + str(lives), True, Color("white"))
        lives_text_rect = lives_text.get_rect(center=(57, 50))
        screen.blit(lives_text, lives_text_rect)

        if game_over:
            end_game_screen.fill((193, 225, 193))
            go_rect = pygame.Rect(WINDOW_SIZE[0] // 2 - 200, WINDOW_SIZE[1] // 2 - 150, 400, 300)
            pygame.draw.rect(end_game_screen, (193, 225, 193), go_rect)
            if lives > 0:
                level_complete_text = EG_font.render("LEVEL COMPLETE!", True, Color("black"))
                level_complete_text_rect = level_complete_text.get_rect(center=(WINDOW_SIZE[0] // 2, 180))
                end_game_screen.blit(level_complete_text, level_complete_text_rect)

                map_button = Button(EG_font, "MAP", Color("black"), pygame.Rect(WINDOW_SIZE[0] // 2 - 75, 250, 150, 50), Color("gray"), Color("light gray"))
                map_button.draw_button(end_game_screen, pygame.mouse.get_pos())

                if clicked and map_button.checkHover(pygame.mouse.get_pos()):
                    play_effect('data/audio/select.wav')
                    world_map.main(difficulty=difficulty, coins=coins_collected)
                    pygame.quit()
                    sys.exit()
            else:
                global musicCounter
                if musicCounter ==0:
                    play_effect('data/audio/lose.wav')
                    musicCounter += 1
                fail_text = EG_font.render("GAME OVER", True, Color("red"))
                fail_text_rect = fail_text.get_rect(center=(WINDOW_SIZE[0] // 2, 180))
                end_game_screen.blit(fail_text, fail_text_rect)

                restart_button = Button(EG_font, "RESTART", Color("black"), pygame.Rect(WINDOW_SIZE[0] // 2 - 100, 250, 200, 50), Color("gray"), Color("light gray"))
                restart_button.draw_button(end_game_screen, pygame.mouse.get_pos())

                if clicked and restart_button.checkHover(pygame.mouse.get_pos()):
                    musicCounter = 0
                    play_effect('data/audio/select.wav')
                    main(difficulty=difficulty)
                    pygame.quit()
                    sys.exit()

            menu_button = Button(EG_font, "MENU", Color("black"), pygame.Rect(WINDOW_SIZE[0] // 2 - 75, 310, 150, 50), Color("gray"), Color("light gray"))
            menu_button.draw_button(end_game_screen, pygame.mouse.get_pos())

            if clicked and menu_button.checkHover(pygame.mouse.get_pos()):
                play_effect('data/audio/select.wav')
                menu.main()
                pygame.quit()
                sys.exit()

            screen.blit(end_game_screen, (0, 0))
        if difficulty:
            try:
                screen.blit(pygame.transform.rotate(hand.frame, -90), (0, 500))
                hand_movement = hand.movement
                if hand_movement[0] == 1:
                    moving_right = True
                    moving_left = False
                    handMove = True
                elif hand_movement[0] == -1:
                    moving_left = True
                    moving_right = False
                    handMove = True
                else:
                    if handMove:
                        moving_right = False
                        moving_left = False
                if hand_movement[1] == 1:
                    if air_timer < 6:
                            player_y_momentum = -5
                
            except TypeError: pass
        pygame.display.update()
        dt = clock.tick(60)

def play_effect(filename):
    pygame.mixer.Channel(4).play(pygame.mixer.Sound(filename))

if __name__ == "__main__":
    pygame.mixer.init()
    main()