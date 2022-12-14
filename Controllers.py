"""
Controllers.py

Simple textbased adventure game with simple UI
and combat and stuff

The Controller

Date-Created: 2022 SEP 13
Date-Last-Modified: 2022 NOV 21
Author: Piyotr Kao
"""
import UI
import GameState

class GameController():

    def __init__(self) -> None:
        self.ad = GameState.Adventure()
        self.ui = UI.MainUI("Fun Game", 600, 600, self.ad)
    
    def start(self) -> None:
        self.ui.mainloop()
    
    @staticmethod
    def update_game(game : GameState.Adventure, name : str, data):
        # To-Do
        pass

class UIController():

    curr_screen : UI.Screen

    def __init__(self) -> None:
        pass