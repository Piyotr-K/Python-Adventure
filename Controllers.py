"""
Controllers.py

Simple textbased adventure game with simple UI
and combat and stuff

The Controller

Date-Created: 2022 SEP 13
Date-Last-Modified: 2022 OCT 12
Author: Piyotr Kao
"""
import UI
import GameState

class GameController():

    def __init__(self) -> None:
        self.ad = GameState.Adventure()
        self.ui = UI.MainUI("Fun Game", 500, 500, self.ad)
    
    def start(self) -> None:
        self.ui.createMenu1()
        self.ui.mainloop()
    
    @staticmethod
    def update_game(game : GameState.Adventure, name : str, data):
        # To-Do
        pass