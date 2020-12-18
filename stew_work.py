# Author:Stew
# Date: 12/16/2020
# Description: This is where I am writing stuff so I don't mess up main

import random as rand

rand.seed()


class Character():
    """This is the class that defines player characters"""

    def __init__(self, hp=10, atk=1):
        """this initializes the player character"""
        self.hp = hp
        self.atk = atk
        self.max_hp = hp

    def take_dmg(self, dmg):
        """takes an int amount of damage dealt to character, can take negative number for
        gaining health
        """
        self.hp -= dmg

    def get_hp(self):
        """returns the current amount of health"""
        return self.hp

    def get_max_hp(self):
        """returns the max health of character"""
        return self.max_hp

    def get_atk_dmg(self):
        """returns the amount of damage character does when it gets correct answer"""
        return self.atk

class Dungeon():
    """class that stores the dungeon"""
    #contains list of 'rooms' which are themselves a list containing the encounter in that room
    #as well as a list of where there are doors in the room and the name of the room

    def __init__(self, num_rooms, depth=8):
        """initializes empty dungeon"""
        self.depth = depth #distance to boss room
        self.map = self._make_board()
        print(self.map)
        self.make_rooms(num_rooms)

    def _make_board(self):
        """returns an A by A size list where A is the size of the game board
         and every value is the input value given
         """
        return [[(num_row,num_col) for num_col in range(self.depth)] for num_row in range(self.depth)]

    #This function doesn't work yet, gonna do it differently than I originally thought
    def make_rooms(self, num_rooms):
        main_route = []
        for num in range(self.depth):
            way = rand.randint(1,3)
            if way == 1:
                main_route.append(['east'])
            if way == 2:
                main_route.append(['north'])
            if way == 3:
                main_route.append(['west'])
        side_rooms = num_rooms - self.depth
        counter = 0



dungeon = Dungeon(14)
