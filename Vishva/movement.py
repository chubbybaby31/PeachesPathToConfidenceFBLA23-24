import pygame, sys, math

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()

pygame.display.set_caption('FBLA 2023-24')

WINDOW_SIZE = (600, 400)

DISPLAY_SIZE = (300, 200)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

display = pygame.Surface(DISPLAY_SIZE)

def load_map(path):
    f = open(path + '.txt', 'r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))
    return game_map

global animation_frames
animation_frames = {}

def load_animation(path, frame_durations):
    global animation_frames
    animation_name = path.split('/')[-1]
    animation_frame_data = []
    n = 0
    for frame in frame_durations:
        animation_frame_id = animation_name + '_' + str(n)
        img_loc = path + '/' + animation_frame_id + '.png'
        animation_image = pygame.image.load(img_loc).convert()
        animation_image = pygame.transform.scale(animation_image, (20, 25))
        animation_image.set_colorkey(Color("white"))
        animation_frames[animation_frame_id] = animation_image.copy()
        for i in range(frame):
            animation_frame_data.append(animation_frame_id)
        n += 1
    return animation_frame_data

def change_action(action_var, frame, new_value):
    if action_var != new_value:
        action_var = new_value
        frame = 0
    return action_var, frame

animation_database = {}
animation_database['run'] = load_animation('run', [3, 6, 6, 6, 3])
animation_database['idle'] = load_animation('idle', [10])

player_action = 'idle'
player_frame = 0
player_flip = False

game_map = load_map('map')

grass_image = pygame.image.load('grass.png')
dirt_image = pygame.image.load('dirt.png')
chest_image = pygame.image.load('chest.png')
door_image = pygame.image.load('door_closed.png')
TILE_SIZE = dirt_image.get_width()

GUI_font = pygame.font.SysFont(None, 25)

confidence_quips = {3: "you rock 3", 4: "you rock 4", 5: "you rock 5"}

confidence_collected = {3: False, 4: False, 5: False}

def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def move(rect, movement, tiles):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    rect.x += movement[0]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    
    rect.y += movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True

    return rect, collision_types

def show_popup(screen, message, popup=False):
    font = pygame.font.SysFont(None, 15)
    text = font.render(message, True, (0, 0, 0))
    if popup:
        text_rect = text.get_rect(center=(DISPLAY_SIZE[0]/2, DISPLAY_SIZE[1] * 7 / 8))
    else: text_rect = text.get_rect(center=(DISPLAY_SIZE[0]/2, DISPLAY_SIZE[1] / 2))
    pygame.draw.rect(screen, (255, 255, 255), text_rect.inflate(2, 2))  
    screen.blit(text, text_rect)

c_pts = 0
max_c_pts = 3

moving_right = False
moving_left = False

player_y_momentum = 0
air_timer = 0

true_scroll = [0, 0]

player_rect = pygame.Rect(50, 50, 20, 25)
test_rect = pygame.Rect(100, 100, 100, 50)

near_chest = False
current_chest_id = None

near_door = False

while True:
    chest_popup_id = None

    display.fill(Color("sky blue"))

    true_scroll[0] += (player_rect.x - true_scroll[0] - 152) / 20
    true_scroll[1] += (player_rect.y - true_scroll[1] - 106) / 20
    scroll = true_scroll.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])

    tile_rects = []
    chests = []
    chest_ids = []
    for y, row in enumerate(game_map):
        for x, tile in enumerate(row):
            if tile == '1':
                display.blit(dirt_image, (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))
            elif tile == '2':
                display.blit(grass_image, (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))
            elif tile == '9':
                display.blit(door_image, (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))
                door_rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE * 2)
            elif int(tile) > 2:
                display.blit(chest_image, (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))
                chests.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                chest_ids.append(int(tile))
            if tile != '0':
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
        player_action, player_frame = change_action(player_action, player_frame, 'run')
        player_flip = False
    elif player_movement[0] < 0:
        player_action, player_frame = change_action(player_action, player_frame, 'run')
        player_flip = True
    elif player_movement[0] == 0:
        player_action, player_frame = change_action(player_action, player_frame, 'idle')

    player_rect, collisions = move(player_rect, player_movement, tile_rects)
    if collisions['bottom']: 
        player_y_momentum = 0
        air_timer = 0
    else: air_timer += 1

    if air_timer > 10:
        player_action, player_frame = change_action(player_action, player_frame, 'idle')

    player_frame += 1
    if player_frame >= len(animation_database[player_action]):
        player_frame = 0
    
    player_img_id = animation_database[player_action][player_frame]
    player_image = animation_frames[player_img_id]

    display.blit(pygame.transform.flip(player_image, player_flip, False), (player_rect.x - scroll[0], player_rect.y - scroll[1]))


    for id, chest in zip(chest_ids, chests):
        distance = math.sqrt((player_rect.x - chest.x)**2 + (player_rect.y - chest.y)**2)
        if distance <= 30 and not near_chest and not confidence_collected[id]:
            chest_popup_id = id
    
    unlocked = True
    for id in chest_ids:
        if not confidence_collected[id]:
            unlocked = False
            break

    if unlocked: door_image = pygame.image.load('door_opened.png')

    door_distance = math.sqrt((player_rect.x - door_rect.x)**2 + (player_rect.y - door_rect.y)**2)
    if door_distance <= 30 and not near_door and not unlocked:
        show_popup(display, "Unlock all " + str(max_c_pts) + " chests to open door", popup=True)
    elif door_distance <= 30: 
        show_popup(display, "Press ENTER to complete level", popup=True)

    if chest_popup_id != None and not confidence_collected[chest_popup_id]:
        show_popup(display, "Press E to open chest", popup=True)
    elif current_chest_id != None:
        show_popup(display, confidence_quips[current_chest_id])
        show_popup(display, "Press ESC to exit", popup=True)


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT and current_chest_id == None :
                moving_right = True
            if event.key == K_LEFT and current_chest_id == None:
                moving_left = True
            if event.key == K_UP:
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
                print("level complete")
                pygame.quit()
                sys.exit()

    screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0, 0))

    c_pts_text = GUI_font.render("CONFIDENCE POINTS: " + str(c_pts) + " / " + str(max_c_pts), True, Color("white"))
    c_pts_text_rect = c_pts_text.get_rect(center=(120, 12))
    screen.blit(c_pts_text, c_pts_text_rect)

    pygame.display.update()
    clock.tick(60)