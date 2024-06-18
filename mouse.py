import cv2
import mediapipe as mp
import numpy as np
import pyautogui as pg
import pygame
from _thread import start_new_thread

class Mouse():
  
    def __init__(self):
        self.frame = None
        self.frame_size = (150, 100)
        # Initialize previous average x-coordinate for swipe detection
        self.cap = cv2.VideoCapture(0)
        start_new_thread(self.get_frame, ())

    
    def get_frame(self):
        while True:
            ret, frame = self.cap.read()    
            # Flip the frame horizontally for a later selfie-view display
            frame = cv2.resize(frame, self.frame_size)
            #frame = cv2.flip(frame, 1)
            # Convert the BGR image to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Process the frame and find hands
            frame = pygame.surfarray.make_surface(frame)
            self.frame = frame