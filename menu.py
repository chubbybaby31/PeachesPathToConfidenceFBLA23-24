import pygame, sys
from pygame.locals import *
from button import Button
import messages
from _thread import start_new_thread


def main():

    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('FBLA 2023-24')
    

    global WINDOW_SIZE
    WINDOW_SIZE = (800, 600)

    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
    bg_img = pygame.image.load("data/images/menuScreen.png")
    bg_img = pygame.transform.scale(bg_img, (900, 600))

    title_font = pygame.font.Font('data/ARCADE_N.TTF', 30)

    while True:
        clicked = False
        screen.blit(bg_img, (0, 0))

        title_text = title_font.render("PEACHE'S PATH TO CONFIDENCE", True, Color("white"))
        title_rect = title_text.get_rect(center=(WINDOW_SIZE[0] // 2, 30))
        screen.blit(title_text, title_rect)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                clicked = True
        
        start_button = Button(title_font, "START", Color("black"), pygame.Rect(WINDOW_SIZE[0] // 2 - 75, 100, 150, 50), Color("white"), Color("pink"))
        start_button.draw_button(screen, pygame.mouse.get_pos())

        instruction_button = Button(title_font, "INSTRUCTIONS", Color("black"), pygame.Rect(WINDOW_SIZE[0] // 2 - 175, 200, 350, 50), Color("white"), Color("pink"))
        instruction_button.draw_button(screen, pygame.mouse.get_pos())

        quit_button = Button(title_font, "QUIT", Color("black"), pygame.Rect(WINDOW_SIZE[0] // 2 - 75, 300, 150, 50), Color("white"), Color("pink"))
        quit_button.draw_button(screen, pygame.mouse.get_pos())

        if clicked and start_button.checkHover(pygame.mouse.get_pos()):
            play_effect('data/audio/select.wav')
            messages.story_line()
            pygame.quit()
            sys.exit()
        elif clicked and instruction_button.checkHover(pygame.mouse.get_pos()):
            play_effect('data/audio/select.wav')
            messages.instructions()
            pygame.quit()
            sys.exit()
        elif clicked and quit_button.checkHover(pygame.mouse.get_pos()):
            play_effect('data/audio/select.wav')
            pygame.quit()
            sys.exit()
            
        pygame.display.update()
        pygame.display.flip()
        dt = clock.tick(60)

def play_bg_music(filename):
    bg_music = pygame.mixer.Sound(filename)
    bg_music.set_volume(0.2)
    pygame.mixer.Channel(0).play(bg_music, -1) 


def play_effect(filename):
    pygame.mixer.Channel(1).play(pygame.mixer.Sound(filename))

if __name__ == '__main__':
    pygame.mixer.init()
    start_new_thread(play_bg_music, ('data/audio/bg_music.wav',))
    main()
    