"""
UI.py

Containing UI Classes

MainUI is the main window

Perhaps we have more windows later that can be added

Date-Created: 2022 SEP 13
Date-Modified: 2022 OCT 03
Author: Piyotr Kao
"""

import tkinter as tk
from typing import List
from PIL import ImageTk, Image

class MainUI():

    def __init__(self, _title : str, _width : int, _height : int) -> None:
        self.window : tk.Tk = tk.Tk(className=_title)
        self.window.iconbitmap("./res/imgs/favicon.ico")
        self.width : int = _width
        self.height : int = _height
        self.btns : List[tk.Button] = []
        self.setup()
    
    def setup(self) -> None:
        sw = self.window.winfo_screenwidth()
        sh = self.window.winfo_screenheight()
        x = (sw // 2) - (self.width // 2)
        y = (sh // 2) - (self.height // 2)

        self.window.geometry(f"{self.width}x{self.height}+{x}+{y}")
        self.mainmenu()
    
    def mainmenu(self) -> None:
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_rowconfigure(1, weight=1)
        self.topFrame = tk.Frame(master=self.window,
                                bg="darkgrey")
        self.topFrame.grid(sticky="nesw")
        self.topFrame.grid_propagate(False)
        self.topFrame.grid_rowconfigure(0, weight=1)
        # self.topFrame.pack(expand=tk.YES, side=tk.TOP, fill=tk.BOTH, anchor=tk.N)
        # self.topFrame.pack_propagate(False)

        self.botFrame = tk.Frame(master=self.window,
                                bg="maroon")
        self.botFrame.grid(sticky="nesw")
        self.botFrame.grid_propagate(False)
        # self.botFrame.pack(expand=tk.YES, side=tk.BOTTOM, fill=tk.BOTH, anchor=tk.S)
        # self.botFrame.pack_propagate(False)

        self.addImgL(0.1, "./res/imgs/zux.png")

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
        
        self.btns.append(
            tk.Button(master = self.botFrame,
            text="Press For Lel",
            command=self.displayText))
        
        self.btns.append(
            tk.Button(master = self.botFrame,
            text="Press For Lel2",
            command=self.displayText))
        
        self.btns[0].grid(row=0,column=0, sticky="w")
        self.btns[1].grid(row=0, column=1, sticky="e")
        self.window.update()
    
    def displayText(self) -> None:
        print("Lel")
    
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