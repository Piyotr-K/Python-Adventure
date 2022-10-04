"""
Adventure.py

Simple textbased adventure game with simple UI
and combat and stuff

Lol

Date-Created: 2022 SEP 13
Date-Modified: 2022 OCT 03
Author: Piyotr Kao
"""
import UI

class Adventure():
    def __init__(self) -> None:
        self.game = UI.MainUI("Fun Gaem", 500, 500)
    
    def start(self) -> None:
        self.game.createMenu1()
        self.game.mainloop()