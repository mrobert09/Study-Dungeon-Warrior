import pygame as pg
import math
from settings import *
from minimap import *
from sprites import *
from stew_work import *

class Game:
    def __init__(self):
        # initialize game window, etc
        self.running = True
        self.dungeon = Dungeon(14)
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

class button:
    """Creation and methods for handling buttons"""

    def __init__(self, color, x, y, width, height, text=''):
        """
        Initializes a button of 'color' color, with the upper left corner at x,y 
        width and height determine size of button
        text is what should be said inside the button
        """
        self.color = color
        self.original_color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rectangle = pg.Rect(x, y, width, height)
        self.text = text

    def draw_button(self, surface):
        """Call this method to draw the button onto the given surface"""
        pg.draw.rect(surface, self.color, self.rectangle)

        if self.text != '':
            text = oswfont32.render(self.text, True, (0,0,0))
            surface.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def mouse_hover_color(self, hover_color):
        """Changes the color of the button when the mouse is hovering over it"""
        mouse_position = pg.mouse.get_pos()
        if mouse_position[0] > self.x and mouse_position[0] < (self.x + self.width) and mouse_position[1] > self.y and mouse_position[1] < (self.y + self.height):
                self.color = hover_color
        else:
            self.color = self.original_color


# create the game object
g = Game()
g.show_start_screen()

#Game Loop
while g.running:
    g.new()
    g.show_go_screen()
