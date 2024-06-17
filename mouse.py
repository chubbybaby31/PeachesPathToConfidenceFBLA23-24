import cv2
import mediapipe as mp
import numpy as np
import pyautogui as pg
import pygame

class Mouse():
  
    def __init__(self):
        self.frame

    
    
    frame_size = (200, 200)


    # Initialize previous average x-coordinate for swipe detection
    
    cap = cv2.VideoCapture(0)

    # Initialize MediaPipe Hands
   

    ret, frame = cap.read()
    
    
    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.resize(frame, frame_size)
    frame = cv2.flip(frame, 1)
    
    
    # Convert the BGR image to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame and find hands
    frame = pygame.surfarray.make_surface(frame)
    

