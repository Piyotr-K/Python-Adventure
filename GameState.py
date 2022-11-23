"""
GameState.py

Classes and helper classes related to
GameState such as levels unlocked, current level
progression in the game and such

Includes main combat loop as well (for now)

2022-OCT-10:
- Combat loop on separate thread test(?)

Date-Created: 2022 OCT 04
Date-Last-Modified: 2022 NOV 21
Author: Piyotr Kao
"""
import threading as th
import time as ti
import Actors as A
import typing as type
import AudioController as au
import Settings as se

class Adventure():

    def __init__(self):
        # List of all actors
        self.actors : type.List[A.Actor] = []
        self.actors.append(A.Player("Test Player", 100))
        self.actors.append(A.Actor("Test Enemy", 100))
        self.p : A.Player = self.actors[0] # Player
        self.e : A.Actor = self.actors[1] # Enemy

    # def combatEval(self) -> None:
        
    def eval_btn(self, _id : int) -> None:
        if _id == 0:
            print("Attack")
            au.play_sfx(0, se.game_volume * .5)
            self.p.attack(self.e)
            print(self.p)
            print(self.e)
        elif _id == 1:
            pass