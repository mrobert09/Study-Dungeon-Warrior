import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    """Player sprite class that takes the game class, x coord, y coord,
    and picture as arguments."""
    def __init__(self, game, x, y, image):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.image.load(image)
        self.rect = self.image.get_rect()
        # defining x and y coordinate velocity, default 0
        self.vx, self.vy = 0, 0
        # sets the location of the sprite in pixels, but since we are using tiles we need to
        # multiply by TILESIZE to get the appropriate coordinate in tiles
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.drawshift_x = 0
        self.drawshift_y = 0

    def get_keys(self):
        # assumes velocity is 0 on both axis unless key is pressed
        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()
        # changes velocity based on the key, uses PLAYER_SPEED from settings.py
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vx = -PLAYER_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vx = PLAYER_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vy = -PLAYER_SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vy = PLAYER_SPEED
        # Fixes diagonals going double speed, 0.7071 is derived from pythragians theorem
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071

    def collision_check(self, dir, sprite_group):
        """Collision checking method. Takes axis (x or y) and sprite group as arguments."""
        if dir == "x":
            # spritecollide has 3 arguments: self, the sprite group you are checking, and
            # True or False depending if you want the object to disappear when you collide
            hits = pg.sprite.spritecollide(self, sprite_group, False)
            if hits:
                # aligns the side of player sprite with side of wall
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                # sets x velocity to 0 due to collision
                self.vx = 0
                self.rect.x = self.x
        if dir == "y":
            hits = pg.sprite.spritecollide(self, sprite_group, False)
            if hits:
                # aligns the top / bottom of player sprite with bottom / top of wall
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                # sets y velocity to 0 due to collision
                self.vy = 0
                self.rect.y = self.y
        return False

    def update(self):
        if self.x > WIDTH - self.drawshift_x:
            self.drawshift_x += -WIDTH
            self.x = -self.drawshift_x
        if self.x < -self.drawshift_x:
            self.drawshift_x += WIDTH
            self.x = WIDTH - self.drawshift_x
        if self.y > HEIGHT - self.drawshift_y:
            self.drawshift_y += -HEIGHT
            self.y = -self.drawshift_y
        if self.y < -self.drawshift_y:
            self.drawshift_y += HEIGHT
            self.y = HEIGHT - self.drawshift_y
        # method for determining velocity
        self.get_keys()
        # updates current position based on velocity * time
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        # collision detection must be done separately for x and y to allow for
        # sliding against a wall while also running into it
        self.rect.x = self.x
        self.collision_check('x', self.game.walls)
        self.collision_check('x', self.game.monsters)
        self.rect.y = self.y
        self.collision_check('y', self.game.walls)
        self.collision_check('y', self.game.monsters)


class Monster(pg.sprite.Sprite):
    """Monster sprite class that takes the game class, x coord, y coord,
    and picture as arguments."""
    def __init__(self, game, x, y, image):
        self.groups = game.all_sprites, game.monsters
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.image.load(image)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
       # self.image.set_colorkey(GREEN)  # makes the green wall transparent, comment out to see them

class Minimap(pg.sprite.Sprite):
    def __init__(self, game, x, y, dungeon):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.dungeon = dungeon
        self.size = 6*TILESIZE
        self.image = pg.Surface((self.size, self.size))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
