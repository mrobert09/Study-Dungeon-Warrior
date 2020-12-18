# Author:Stew
# Date: 12/16/2020
# Description: This is where I am writing stuff so I don't mess up main

import Random

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