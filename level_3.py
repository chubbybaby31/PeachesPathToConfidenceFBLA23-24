import pygame, sys, math
import data.engine as e
from pygame.locals import *
from button import Button
import menu
import messages
from mouse import Mouse

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

def main(difficulty, coins_col):

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

    game_map = load_map('map_3')

    grass_image = pygame.image.load('data/images/gravel.png')
    dirt_image = pygame.image.load('data/images/stone.png')
    chest_image = pygame.image.load('data/images/chest.png')
    coin_image = pygame.image.load('data/images/coin_angle.png')
    safe_image = pygame.image.load('data/images/safe.png')
    safe_image = pygame.transform.scale(safe_image, (32, 32))
    food_image = pygame.image.load('data/images/food_basket.png')
    food_image = pygame.transform.scale(food_image, (32, 32))
    door_image = safe_image
    mountain_bg = pygame.image.load('data/images/mountain.jpeg')
    mountain_bg = pygame.transform.scale(mountain_bg, DISPLAY_SIZE)
    TILE_SIZE = dirt_image.get_width()

    GUI_font = pygame.font.Font('data/ARCADE_N.TTF', 10)
    EG_font = pygame.font.Font('data/ARCADE_N.TTF', 25)

    confidence_quips = {3: "Face Your Fears: Step out of your comfort zone and confront the things you're afraid of. Each time you face a fear, you gain strength and self-assurance.", 
                        4: "Celebrate Your Successes: Take time to acknowledge and celebrate your achievements. This reinforces the belief in your abilities and talents.", 
                        5: "Surround Yourself with Supportive People: Spend time with people who uplift and encourage you. Positive reinforcement from friends and family can greatly impact your self-confidence."}

    confidence_collected = {3: False, 4: False, 5: False}

    c_pts = 0
    max_c_pts = 3

    moving_right = False
    moving_left = False

    player_y_momentum = 0
    air_timer = 0

    true_scroll = [0, 0]

    player = e.entity(0, 500, 20, 25, 'player')

    enemies = []
    enemies.append([2, 0, e.entity(700, 10, 28, 20, 'enemy')])
    enemies.append([2, 0, e.entity(500, 30, 28, 20, 'enemy')])
    enemies.append([2, 0, e.entity(270, 75, 28, 20, 'enemy')])
    enemies.append([2, 0, e.entity(50, 110, 28, 20, 'enemy')])
    enemies.append([2, 0, e.entity(400, 190, 28, 20, 'enemy')])
    enemies.append([2, 0, e.entity(1200, 235, 28, 20, 'enemy')])
    enemies.append([2, 0, e.entity(800, 250, 28, 20, 'enemy')])
    enemies.append([2, 0, e.entity(900, 250, 28, 20, 'enemy')])
    enemies.append([2, 0, e.entity(1750, 410, 28, 20, 'enemy')])
    enemies.append([2, 0, e.entity(1100, 460, 28, 20, 'enemy')])
    enemies.append([2, 0, e.entity(400, 475, 28, 20, 'enemy')])
    enemies.append([2, 0, e.entity(1442, 475, 28, 20, 'enemy')])
    enemies.append([2, 0, e.entity(644, 510, 28, 20, 'enemy')])
    near_chest = False
    current_chest_id = None

    near_door = False

    lives = 20
    invincible = False
    invincible_timer = 0
    game_over = False
    food_aquired = False
    food_showing = False
    safe_timer = 0
    food_timer = 0
    handMoved = False
    coins_collected = coins_col
    coins_collected_pos = []
    while True:
        clicked = False
        if player.y >= 600:
            lives = 0

        if lives <= 0:
            game_over = True

        if food_aquired:
            safe_timer += dt

        if food_showing:
            food_timer += dt
        
        if safe_timer >= 1500:
            food_showing = True
            door_image = food_image
        
        if food_timer >= 3000:
            game_over = True

        chest_popup_id = None

        display.fill(Color("sky blue"))
        display.blit(mountain_bg, (0, 0))

        true_scroll[0] += (player.x - true_scroll[0] - 152) / 20
        true_scroll[1] += (player.y - true_scroll[1] - 106) / 20
        scroll = true_scroll.copy()
        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])

        tile_rects = []
        chests = []
        chest_ids = []
        enemy_borders = []
        coins = []
        for y, row in enumerate(game_map):
            for x, tile in enumerate(row):
                if tile == '*' or tile == 'd' or tile == 'g': 
                    enemy_borders.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                    #print(x * TILE_SIZE , y * TILE_SIZE)
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
        #print('\n')
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

        if unlocked: door_image = safe_image

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
                lives -= 1
                invincible = True

        door_distance = math.sqrt((player.x - door_rect.x)**2 + (player.y - door_rect.y)**2)
        if door_distance <= 30 and not near_door and not unlocked:
            show_popup(display, "Unlock all " + str(max_c_pts) + " chests to open safe", popup=True)
        elif door_distance <= 30 and not food_aquired: 
            show_popup(display, "Press ENTER to open safe", popup=True)

        if chest_popup_id != None and not confidence_collected[chest_popup_id]:
            show_popup(display, "Press E to open chest", popup=True)
        elif current_chest_id != None:
            show_popup(display, confidence_quips[current_chest_id])
            show_popup(display, "Press ESC to exit", popup=True)

        if invincible:
            invincible_timer += dt
        if invincible_timer >= 3000:
            invincible_timer = 0
            invincible = False

        for coin in coins:
            if player.obj.rect.colliderect(coin):
                coins_collected_pos.append((coin.x, coin.y))
                coins_collected += 1

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and not difficulty:
                if event.key == K_RIGHT and current_chest_id == None :
                    moving_right = True
                    handMoved = False
                if event.key == K_LEFT and current_chest_id == None:
                    moving_left = True
                    handMoved = False
                if event.key == K_UP:
                    handMoved = False
                    if air_timer < 6:
                        player_y_momentum = -5
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    moving_right = False
                if event.key == K_LEFT:
                    moving_left = False
                if event.key == K_e and chest_popup_id != None:
                    confidence_collected[chest_popup_id] = True
                    current_chest_id = chest_popup_id
                    c_pts += 1
                if event.key == K_ESCAPE:
                    current_chest_id = None
                if event.key == K_RETURN and unlocked:
                    food_aquired = True
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

                map_button = Button(EG_font, "CONTINUE", Color("black"), pygame.Rect(WINDOW_SIZE[0] // 2 - 100, 250, 200, 50), Color("gray"), Color("light gray"))
                map_button.draw_button(end_game_screen, pygame.mouse.get_pos())

                if clicked and map_button.checkHover(pygame.mouse.get_pos()):
                    messages.final()
                    pygame.quit()
                    sys.exit()

            else:
                fail_text = EG_font.render("GAME OVER", True, Color("red"))
                fail_text_rect = fail_text.get_rect(center=(WINDOW_SIZE[0] // 2, 180))
                end_game_screen.blit(fail_text, fail_text_rect)

                restart_button = Button(EG_font, "RESTART", Color("black"), pygame.Rect(WINDOW_SIZE[0] // 2 - 100, 250, 200, 50), Color("gray"), Color("light gray"))
                restart_button.draw_button(end_game_screen, pygame.mouse.get_pos())

                if clicked and restart_button.checkHover(pygame.mouse.get_pos()):
                    main(coins_col)
                    pygame.quit()
                    sys.exit()

            menu_button = Button(EG_font, "MENU", Color("black"), pygame.Rect(WINDOW_SIZE[0] // 2 - 75, 310, 150, 50), Color("gray"), Color("light gray"))
            menu_button.draw_button(end_game_screen, pygame.mouse.get_pos())

            if clicked and menu_button.checkHover(pygame.mouse.get_pos()):
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
        else:
            pygame.display.update()
            dt = clock.tick(60)

if __name__ == "__main__":
    main(0)