"""
UI.py

Containing UI Classes

MainUI is the main window

Perhaps we have more windows later that can be added

Date-Created: 2022 SEP 13
Date-Last-Modified: 2022 NOV 21
Author: Piyotr Kao
"""

import tkinter as tk
import GameState as gs
from typing import List
from PIL import ImageTk, Image

class Screen():
    
    id : int = 0

    def __init__(self, _name : str, _parent : tk.Widget) -> None:
        """
        Binds all set widgets to parent widget and takes a name
        """
        Screen.id += 1
        self.parent : tk.Widget = _parent
        self.name = _name
    
    def setup(self) -> None:
        pass

    def show(self) -> None:
        pass
    
    def set_row_col(self, _f : tk.Frame, _RowCols : str) -> None:
        """
        Sets up the given frame giving 1 weigth to the total number of cols
        and rows desired
        """
        r, c = _RowCols.split("x")
        r = int(r)
        c = int(c)

        for x in range(r):
            _f.grid_rowconfigure(x, weight=1)
        
        for x in range(c):
            _f.grid_columnconfigure(x, weight=1)

class MainMenu(Screen):
    """
    Class representing the main menu screen
    Contains name and other useful properties for the screen
    """

    def __init__(self, _name : str, _parent : tk.Widget) -> None:
        super().__init__(_name, _parent)
        self.setup()
    
    def setup(self) -> None:
        bg_color = "darkgrey"
        self.topFrame = tk.Frame(master=self.parent, bg=bg_color)
        self.title : tk.Label = tk.Label(master = self.topFrame,
                                        text=MainUI.gameTitle,
                                        font=("Consolas", 20),
                                        bg=bg_color)
        self.btn_play : tk.Button = tk.Button(master = self.topFrame,
                                        text="Play Now!",
                                        font=("Consolas", 16),
                                        borderwidth=5)

        self.btn_quit : tk.Button = tk.Button(master = self.topFrame,
                                        text="no :(",
                                        font=("Consolas", 16),
                                        borderwidth=5)

        self.title.place(relx=.5,rely=.4,anchor="c")

        self.btn_play.place(relx=.5,rely=.5,anchor="c")

        self.btn_quit.place(relx=.5,rely=.8,anchor="c")
    
    def show(self) -> None:
        self.set_row_col(self.parent, "1x1")
        self.topFrame.grid(row=0,column=0, sticky="nesw")
        self.topFrame.grid_propagate(False)

class CombatMenu(Screen):
    """
    Class representing the combat screen
    Contains name and other useful properties for the screen
    """

    def __init__(self, _name : str, _parent : tk.Widget) -> None:
        super().__init__(_name, _parent)
        self.setup()
    
    def setup(self) -> None:
        self.topFrame = tk.Frame(master=self.parent,
                                bg="darkgrey")

        self.botFrame = tk.Frame(master=self.parent,
                                bg="lightgrey")
        
        self.addImgL(0.1, "./res/imgs/zux.png")

        self.createMenu1()
    
    def addImgL(self, _size : int, _img : str) -> None:
        tmp_img = Image.open(_img)
        c_w = int(tmp_img.width * _size)
        c_h = int(tmp_img.height * _size)
        resized = tmp_img.resize((c_w, c_h),  Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(resized)
        self.lbl = tk.Label(master=self.topFrame, image=self.img)
        self.lbl.place(relx=.5, rely=.5, anchor="c")
    
    def createMenu1(self) -> bool:
        self.btns : List[tk.Button] = []
        
        # set botFrame to a 2x2 grid
        self.set_row_col(self.botFrame, "2x2")

        options = ["Attack", "Defend", "Bag", "Run"]
        btn_font = ("Consolas", 15)
        
        # Need the lambda default keyword expressions
        for x in range(4):
            self.btns.append(
                tk.Button(master = self.botFrame,
                text=options[x],
                font=btn_font))

        p_x = 40
        p_y = 20
        
        self.btns[0].grid(row=0,column=0, sticky="nesw", padx=p_x, pady=p_y)
        self.btns[1].grid(row=0, column=1, sticky="nesw", padx=p_x, pady=p_y)
        self.btns[2].grid(row=1, column=0, sticky="nesw", padx=p_x, pady=p_y)
        self.btns[3].grid(row=1, column=1, sticky="nesw", padx=p_x, pady=p_y)

    def show(self) -> None:
        self.set_row_col(self.parent, "2x1")
        self.topFrame.grid(row=0, column=0,sticky="nesw")
        self.topFrame.grid_propagate(False)
        self.botFrame.grid(row=1, column=0,sticky="nesw")
        self.botFrame.grid_propagate(False)

class MainUI():
    """
    Contains the root of the tkinter object
    """

    gameTitle : str = "Super Fun Game Please Play"

    def __init__(self, _title : str, _width : int, _height : int, _game : gs.Adventure) -> None:
        self.window : tk.Tk = tk.Tk(className=_title)
        self.window.iconbitmap("./res/imgs/favicon.ico")
        self.width : int = _width
        self.height : int = _height
        self.game : gs.Adventure = _game
        self.currFrame : tk.Frame = tk.Frame(master=self.window, width=_width, height=_height)
        self.currFrame.grid(row=0,column=0)
        self.currFrame.grid_propagate(False)
        self.Screens : List[Screen] = []
        self.setup()
    
    def setup(self) -> None:
        sw = self.window.winfo_screenwidth()
        sh = self.window.winfo_screenheight()
        x = (sw // 2) - (self.width // 2)
        y = (sh // 2) - (self.height // 2)

        self.window.geometry(f"{self.width}x{self.height}+{x}+{y}")

        self.Screens.append(MainMenu("MainMenu1", self.currFrame))
        self.Screens.append(CombatMenu("CombatMenu1", self.currFrame))

        for s in self.Screens:
            s.setup()
        
        tmp : MainMenu = self.Screens[0]
        tmp.btn_play.configure(command= lambda : self.change_screens(0, 1))
        tmp.btn_quit.configure(command=self.exit)

        tmp2 : CombatMenu = self.Screens[1]
        for i in range(len(tmp2.btns)):
            tmp2.btns[i].configure(command=lambda x=i: self.game.eval_btn(x))
        
        print(tmp2.btns)
        
        self.Screens[0].show()
        # self.mainMenu()
    
    def addImgC(self, _x : int, _y : int, _size : float,  _pos : tk.ANCHOR, _img : str) -> None:
        tmp_img = Image.open(_img)
        c_w = int(tmp_img.width * _size)
        c_h = int(tmp_img.height * _size)

        self.resized = tmp_img.resize((c_w, c_h),  Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.resized)
        self.img.width = self.width
        self.img.height = self.height
        self.canvas.create_image(_x, _y, anchor=_pos, image=self.img)
    
    def mainloop(self) -> None:
        self.window.mainloop()
    
    def exit(self) -> None:
        print("Game Closing...")
        print("Bye!")
        self.window.destroy()
    
    def clear(self, _w : tk.Frame, _hard : bool = False) -> None:
        """
        Clear all widgets from _w, if _hard is enabled, it will destroy() all widgets
        """

        # Necessary because widget.children returns the widget itself
        _w = list(_w.children.values())[0] # get the widget's children by going 1 layer deeper

        while list(_w.children.values()) != []:
            key, value = list(_w.children.items())[0] # Delete using pop() from the front
            # print(f"Key: {key}, Value: {value}")
            tmp : tk.Widget = _w.children.pop(key)
            if _hard:
                tmp.destroy()

    
    def test_combat(self) -> None:
        self.change_screens(self.currFrame, self.mainMenu())

    def change_screens(self, _scNumStart : int, _scNumRes : int) -> None:
        """
        Changes "screens" by way of forgetting the old frame and setting the new one
        """
        self.clear(self.Screens[_scNumStart].parent, False)
        self.Screens[_scNumRes].show()
    
    def set_row_col(self, _f : tk.Frame, _RowCols : str) -> None:
        """
        Sets up the given frame giving 1 weight to the total number of cols
        and rows desired
        """
        r, c = _RowCols.split("x")
        r = int(r)
        c = int(c)

        for x in range(r):
            _f.grid_rowconfigure(x, weight=1)
        
        for x in range(c):
            _f.grid_columnconfigure(x, weight=1)
