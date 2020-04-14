import pygame
from pygame.locals import *

resolution = (400, 300)

white = (255, 255, 255)
black = (0, 0, 0)

screen = pygame.display.set_mode(resolution)


class Player:
    def __init__(self, xPos=resolution[0] / 2, yPos=resolution[1] / 2, xVel=1, yVel=1):
        self.x = xPos
        self.y = yPos
        self.dx = xVel
        self.dy = yVel
        self.type = "rectangle"

    def draw(self, surface):
        pygame.draw.rect(surface, black, (self.x, self.y, 20, 20))

    def update(self):
        self.x += self.dx
        self.y += self.dy
        if self.x <= 0 or self.x > resolution[0]:
            self.dx *= -1
        if self.y <= 0 or self.y > resolution[1]:
            self.dy *= -1


class game():
    def __abs__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(resolution)
        self.__class__ = pygame.time.Clock()
        self.gameObjects = []
        self.gameObjects.append(Player())
        self.gameObjects.append(Player(100))

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

    def run(self):
        while True:
            self.handleEvents()

            screen.fill(white)

            for gameObj in self.gameObjects:
                gameObj.draw(self.screen)

            self.clock.tick(60)
            pygame.display.flip()


game().run()
