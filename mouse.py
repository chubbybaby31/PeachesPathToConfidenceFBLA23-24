import cv2
import mediapipe as mp
import numpy as np
import pyautogui as pg
import pygame
from _thread import start_new_thread
import math

class Mouse():
  
    def __init__(self):
        self.frame = None
        self.frame_size = (150, 100)
        self.cap = cv2.VideoCapture(0)
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils
        start_new_thread(self.get_frame, ())
        self.movement = [0,0]
        self.open = False
        self.exit = False
        self.SWIPE_THRESHOLD = 55
        self.swipedown_threshold = -55
        self.history_len = 10
        self.y_history = []
        self.counter1 = 0
        self.counter2 = 0
      
    
    def get_frame(self):
        while True:
            
            ret, frame = self.cap.read()
            # Flip the frame horizontally for a later selfie-view display
            frame = cv2.resize(frame, self.frame_size)
            #frame = cv2.flip(frame, 1)
            # Convert the BGR image to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Process the frame and find hands
            results = self.hands.process(frame)   
            try:
                frame = cv2.rectangle(frame, (0, 0), (50, 100), (255, 0, 0), 1)
                frame = cv2.rectangle(frame, (50, 0), (100, 100), (0, 255, 0), 1)
                frame = cv2.rectangle(frame, (100, 0), (150, 100), (0, 0, 255), 1)
            except TypeError:
                continue
            self.finger_pos = {8: None, 4: None}
            if results.multi_hand_landmarks:
                for handLms in results.multi_hand_landmarks:
                    for id, lm in enumerate(handLms.landmark):
                        h, w, c = frame.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        if id == 8 or id == 4:
                            self.finger_pos[id] = (cx * 2560 / 640, cy * 1440 / 480)
                            cv2.circle(frame, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
                    
            
                    y_coord =  (self.finger_pos[8][1] + self.finger_pos[4][1]) / 2
                    self.y_history.append(y_coord)
                    
                    if len(self.y_history) > self.history_len:
                        self.y_history.pop(0)
                    
                    if len(self.y_history) == self.history_len:
                        y_diff = self.y_history[0] - self.y_history[-1]
                        if y_diff > self.SWIPE_THRESHOLD and self.counter2 == 0:
                            self.open = True
                            self.exit = False
                            self.counter1 == 0
                        elif y_diff < self.swipedown_threshold and self.counter1 == 0:
                            self.exit = True
                            self.open = False
                            self.counter2 == 0
                        else:
                            self.open = False
                            self.exit = False

            else: 
                self.finger_pos[8] = (201, 200)
                self.finger_pos[4] = (201, 200)


            frame = pygame.surfarray.make_surface(frame)
            self.frame = frame
            xPos = (int(self.finger_pos[8][0]) + int(self.finger_pos[4][0]))/2
            if xPos < 200: 
                self.movement[0] = 1
            elif xPos > 400:
                self.movement[0] = -1
            else:
                self.movement[0] = 0
            
            

            
            distance = math.sqrt(((self.finger_pos[8][0]-self.finger_pos[4][0])**2)+((self.finger_pos[8][1]-self.finger_pos[4][1])**2))
            if int(distance) > 50: self.movement[1] = 1
            else: self.movement[1] = 0