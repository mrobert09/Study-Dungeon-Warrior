import pygame as pg
from settings import *
from sprites import *
import time

class Room:

    def __init__(self, game, bgimage, L, U, R, D):
        self.background = pg.image.load(bgimage)
        self.game = game
        self.L = L
        self.U = U
        self.R = R
        self.D = D

    def get_background(self):
        return self.game.screen.blit(self.background, (0, 0))

    def room_creation(self):
        self.game.walls = pg.sprite.Group()
        self.game.monsters = pg.sprite.Group()
        self.create_walls()

    def create_walls(self):
        for row, tiles in enumerate(self.game.map.map_data):
            for col, tile in enumerate(tiles):
                if tile == "1":
                    Wall(self.game, col, row)
                if tile == "M":
                    self.game.monster1 = Monster(self.game, col, row, 'Images/monster.png')