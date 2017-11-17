"""
Created on Fri Nov 17 01:50:04 2017

@author: meixx115
"""
import tkinter as tk
import time
from tkinter import *


class TetrisRoot:
     def __init__(self):
         self.root = tk.Tk()
         self.label = tk.Label(text="")
         self.label.pack()
         self.update_clock()
         self.root.mainloop()
         
     def update_clock(self):
         now = time.strftime("%H:%M:%S")
         self.label.configure(text=now)
         self.root.after(1000, self.update_clock)
         
         


class TetrisCanvas:
    def __init__(self):
        self.canvas = tk.Canvas(bg="grey")
    
    def place(self, height, width, x, y):
        self.canvas.height = height
        self.canvas.width  = width
        self.canvas.canvasx(x)
        self.canvas.canvasy(y)
    
    def unplace(self):
        
        

class TetrisButton:
    def __init__(self, label, color):
        self.button = tk.Button(   )
        
        
        
class TetrisRect:
    def __init__(self, wrapped_canvas, a, b, c, d, color):
        upwrapped_canvas = wrapped_canvas.canvas
        self.rect = 
        

def mainLoop:
    tk.mainloop()
def 
        