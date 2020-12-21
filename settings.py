import pygame
pygame.init()
# colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BROWN = (51, 17, 0)

# game settings
# WIDTH = 1024  # divisible by 16, 32, and 64
# HEIGHT = 768  # divisible by 16, 32, and 64
WIDTH = 608
HEIGHT = 608
FPS = 60
BGCOLOR = BLACK
TITLE = "Study Dungeon Warrior"

# grid
TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Player settings
PLAYER_SPEED = 1000

#Sound Effects
oof = pygame.mixer.Sound("Sounds/Oof.wav")
hiyaa = pygame.mixer.Sound("Sounds/hiyaa.wav")
bebetter = pygame.mixer.Sound("Sounds/bebetter.wav")
bossdead = pygame.mixer.Sound("Sounds/bossdead.wav")
bosstentacles = = pygame.mixer.Sound("Sounds/bosstentacles.wav")
door = pygame.mixer.Sound("Sounds/door.wav")
getgood = pygame.mixer.Sound("Sounds/getgood.wav")
monsterohsnap = pygame.mixer.Sound("Sounds/monsterohsnap.wav")
ohnomonster = pygame.mixer.Sound("Sounds/ohnomonster.wav")
wall = pygame.mixer.Sound("Sounds/wall.wav")

#Fonts
oswfont32 = pygame.font.Font("Fonts/Oswald-VariableFont_wght.ttf", 32)