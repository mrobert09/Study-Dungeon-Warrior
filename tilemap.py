import pygame as pg
from settings import *

class Map:
    def __init__(self, filename):
        with open(filename, 'rt') as tilemap:
            self.map_data = []
            for line in tilemap:
                self.map_data.append(line)

        self.tilewidth = len(self.map_data[0])
        self.tileheight = len(self.map_data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE

class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = target.drawshift_x
        y = target.drawshift_y
        self.camera = pg.Rect(x, y, self.width, self.height)