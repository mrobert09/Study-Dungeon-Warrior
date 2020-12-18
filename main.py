import pygame as pg
import math
from settings import *
from sprites import *

class Game:
    def __init__(self):
        # initialize game window, etc
        self.running = True
        pg.init()
        pg.mixer.init()  # in case we want to add sound later
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.icon = pg.image.load("Images/icon-sword.png")
        pg.display.set_icon(self.icon)
        self.clock = pg.time.Clock()  # used to set FPS later
        self.background = pg.image.load('Images/BasicRoom.png')

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.monsters = pg.sprite.Group()
        self.player = Player(self, 8, 14, 'Images/actor.png')
        for x in range(0, 19):
            Wall(self, x, 0)
        for x in range(0, 19):
            Wall(self, x, 17)
        for y in range(0, 17):
            Wall(self, 0, y)
        for y in range(0, 17):
            Wall(self, 18, y)
        self.monster1 = Monster(self, 8, 1, 'Images/monster.png')
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            # dt = how much time the previous frame took, given in milliseconds
            self.dt = self.clock.tick(FPS) / 1000  # dividing by 1000 to convert to seconds
            # the three main components of the cycle
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - update
        self.all_sprites.update()  # passing dt to make movement speed not tied to frame rate, but time

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window. Exits both the game event and the window.
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False


    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        # Game Loop - draw
        self.screen.blit(self.background, (0,0))
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        # always do last after drawing everything
        pg.display.flip()  # very important to make less intensive / slow

    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        # game over/continue
        pass

# create the game object
g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()
