import random
import pygame.image
import service

class Pelota:
    def __init__(self, img):
        self.img = pygame.image.load(img).convert_alpha() # ball image
        self.width, self.height = self.img.get_size() # ball size

        # Balls Position at the beginning
        self.x = service.HORIZONTAL_WINDOW / 2 - self.width / 2
        self.y = service.VERTICAL_WINDOW / 2 - self.height / 2

        # Ball's direction Movement
        self.dir_x = random.choice([-5, 5])
        self.dir_y = random.choice([-5, 5])

        #Puntuation
        self.puntuation = 0
        self.puntuationIA = 0

    def mov(self):
        self.x += self.dir_x
        self.y += self.dir_y

    def bounce(self):
        if self.x <= 0:
            self.restart()
            self.puntuationIA += 1
        if self.x >= service.HORIZONTAL_WINDOW:
            self.restart()
            self.puntuation += 1
        if self.y <= 0:
            self.dir_y = -self.dir_y
        if self.y + self.height >= service.VERTICAL_WINDOW:
            self.dir_y = -self.dir_y

    def restart(self):
        self.x = service.HORIZONTAL_WINDOW /2 - self.width / 2
        self.y = service.VERTICAL_WINDOW /2 - self.height
        self.dir_x = -self.dir_x
        self.dir_y = random.choice([-5, 5])