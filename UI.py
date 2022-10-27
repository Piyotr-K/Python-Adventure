"""
UI.py

Containing UI Classes

MainUI is the main window

Perhaps we have more windows later that can be added

Date-Created: 2022 SEP 13
Date-Last-Modified: 2022 OCT 27
Author: Piyotr Kao
"""

import tkinter as tk
import GameState as gs
from typing import List
from PIL import ImageTk, Image

class MainUI():

    gameTitle : str = "Super Fun Game Please Play"

    def __init__(self, _title : str, _width : int, _height : int, _game : gs.Adventure) -> None:
        self.window : tk.Tk = tk.Tk(className=_title)
        self.window.iconbitmap("./res/imgs/favicon.ico")
        self.width : int = _width
        self.height : int = _height
        self.btns : List[tk.Button] = []
        self.game : gs.Adventure = _game
        self.setup()
    
    def setup(self) -> None:
        sw = self.window.winfo_screenwidth()
        sh = self.window.winfo_screenheight()
        x = (sw // 2) - (self.width // 2)
        y = (sh // 2) - (self.height // 2)

        self.window.geometry(f"{self.width}x{self.height}+{x}+{y}")
        self.mainMenu()
        # self.combatMenu()
    
    def mainMenu(self) -> None:
        bg_color = "darkgrey"
        self.set_row_col(self.window, "1x1")
        self.topFrame : tk.Frame = tk.Frame(master = self.window, bg=bg_color)
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
                                        borderwidth=5,
                                        command=self.exit)
        
        self.topFrame.grid(row=0,column=0, sticky="nesw")
        self.topFrame.grid_propagate(False)

        self.title.place(relx=.5,rely=.4,anchor="c")

        self.btn_play.place(relx=.5,rely=.5,anchor="c")

        self.btn_quit.place(relx=.5,rely=.8,anchor="c")
    
    def combatMenu(self) -> None:
        self.set_row_col(self.window, "2x1")

        self.topFrame = tk.Frame(master=self.window,
                                bg="darkgrey")
        self.topFrame.grid(row=0, column=0,sticky="nesw")
        self.topFrame.grid_propagate(False)

        self.botFrame = tk.Frame(master=self.window,
                                bg="lightgrey")
        self.botFrame.grid(row=1, column=0,sticky="nesw")
        self.botFrame.grid_propagate(False)

        self.addImgL(0.1, "./res/imgs/zux.png")

        self.createMenu1()

        # self.canvas_w = self.width - 20
        # self.canvas_h = self.height // 2
        # self.canvas = tk.Canvas(master=self.topFrame, width=self.canvas_w, height=self.canvas_h, background="gray")

        # self.addImgC(self.canvas_w // 2, self.canvas_h // 2, 1, tk.CENTER, './res/imgs/zux.png')
    
    def addImgL(self, _size : int, _img : str) -> None:
        tmp_img = Image.open(_img)
        c_w = int(tmp_img.width * _size)
        c_h = int(tmp_img.height * _size)
        resized = tmp_img.resize((c_w, c_h),  Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(resized)
        self.lbl = tk.Label(master=self.topFrame, image=self.img)
        self.lbl.pack()
    
    def createMenu1(self) -> bool:
        if self.btns != []:
            for x in self.btns:
                x.grid_forget()
            self.btns.clear()
        
        # set botFrame to a 2x2 grid
        self.set_row_col(self.botFrame, "2x2")

        options = ["Attack", "Defend", "Bag", "Run"]
        btn_font = ("Consolas", 15)
        
        # Need the lambda default keyword expressions
        for x in range(4):
            self.btns.append(
                tk.Button(master = self.botFrame,
                text=options[x],
                font=btn_font,
                command = lambda x=x: self.game.eval_btn(x)))

        p_x = 40
        p_y = 20
        
        self.btns[0].grid(row=0,column=0, sticky="nesw", padx=p_x, pady=p_y)
        self.btns[1].grid(row=0, column=1, sticky="nesw", padx=p_x, pady=p_y)
        self.btns[2].grid(row=1, column=0, sticky="nesw", padx=p_x, pady=p_y)
        self.btns[3].grid(row=1, column=1, sticky="nesw", padx=p_x, pady=p_y)
    
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
