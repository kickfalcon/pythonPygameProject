import random
import pygame.image
import service
from Components.Pelota import Pelota

class Raqueta:
    def __init__(self):
        #Properties
        self.img = pygame.image.load("raqueta.png").convert_alpha()
        self.width, self.height = self.img.get_size()
        #Position
        self.x = 0
        self.y = service.VERTICAL_WINDOW / 2 - self.height / 2
        self.dir_y = 0

    def mov(self):
        self.y += self.dir_y
        if self.y <= 0:
            self.y = 0
        if self.y + self.height >= service.VERTICAL_WINDOW:
            self.y = service.VERTICAL_WINDOW - self.height

    def movAI(self, Pelota):
        if self.y > Pelota.y:
            self.dir_y = -3
        elif self.y < Pelota.y:
            self.dir_y = 3
        else:
            self.dir_y = 0

        self.y += self.dir_y

    def beatTheBall(self, Pelota):
        if(
            Pelota.x < self.x + self.width
            and Pelota.x > self.x
            and Pelota.y + Pelota.height > self.y
            and Pelota.y < self.y + self.height
        ):
            Pelota.dir_x = -Pelota.dir_x
            Pelota.x = self.x + self.width

    def beatTheBallAI(self, Pelota):
        if(
            Pelota.x + Pelota.width > self.x
            and Pelota.x < self.x + self.width
            and Pelota.y + Pelota.height > self.y
            and Pelota.y < self.y + self.height
        ):
            Pelota.dir_x = -Pelota.dir_x
            Pelota.x = self.x - Pelota.width