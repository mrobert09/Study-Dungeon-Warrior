import pygame as pg
from settings import *
from sprites import *

class Room:

    def __init__(self, game, bgimage, L, U, R, D, name):
        self.background = pg.image.load(bgimage)
        self.game = game
        self.L = L
        self.U = U
        self.R = R
        self.D = D
        self.name = name
        self.room_creation()

    def get_background(self):
        return self.game.screen.blit(self.background, (0, 0))

    def room_creation(self):
        self.game.walls = pg.sprite.Group()
        self.game.monsters = pg.sprite.Group()
        self.create_walls()

        self.game.monster1 = Monster(self.game, 8, 1, 'Images/monster.png')

    def create_walls(self):
        if self.L:
            for y in range(0, 8):
                Wall(self.game, 0, y)
            for y in range(10, 17):
                Wall(self.game, 0, y)
        elif not self.L:
            for y in range(0, 17):
                Wall(self.game, 0, y)
        if self.U:
            for x in range(0, 9):
                Wall(self.game, x, 0)
            for x in range(11, 19):
                Wall(self.game, x, 0)
        elif not self.U:
            for x in range(0, 19):
                Wall(self.game, x, 0)
        if self.R:
            for y in range(0, 8):
                Wall(self.game, 18, y)
            for y in range(10, 17):
                Wall(self.game, 18, y)
        elif not self.R:
            for y in range(0, 17):
                Wall(self.game, 18, y)
        if self.D:
            for x in range(0, 9):
                Wall(self.game, x, 17)
            for x in range(11, 19):
                Wall(self.game, x, 17)
        elif not self.D:
            for x in range(0, 19):
                Wall(self.game, x, 17)
