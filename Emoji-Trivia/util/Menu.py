import pygame
import os
import random
import math
pygame.init()
import sys




D2imgs= (math.pi * 2) / 360
Direction_vector = list([[math.cos(D2imgs * degrees), math.sin(D2imgs * degrees)] for degrees in range(360)])

class Mainmenu():
    x = 0.0
    y = 0.0
    def __init__(self, imgsrc,rec,WID,HEIG,WIN):
        global Direction_vector
        self.imgsrc = imgsrc
        self.r = rec
        self.WID = WID 
        self.HEIG = HEIG 
        self.WIN = WIN
        
        self.x += random.randint(self.r.center[0], WID - self.r.center[0])
        self.y += random.randint(self.r.center[1], HEIG - self.r.center[1])

        self.dx, self.dy = Direction_vector[random.randint(0, 359)]


    def draw(self):
        
        self.WIN.blit(self.imgsrc, (self.x - self.r.center[0], self.y - self.r.center[1]))
        


        self.x += self.dx 
        self.y += self.dy  
        

        if self.y <= self.r.center[0] or self.x >= self.WID - self.r.center[0]:
            self.dx = -self.dx

        if self.y <= self.r.center[1] or self.y>= self.HEIG - self.r.center[1]:
            self.dy = -self.dy

    






















    