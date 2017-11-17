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
         self.root.title("Tetris")
         back = tk.Frame(root, width=205, height=605, bg='lightblue')
         back.pack()
         return self.root
         
     def bind(char, callback):
         self.root.bind(char, callback)


class TetrisCanvas:
    def __init__(self):
        self.canvas = tk.Canvas(bg="grey")
        return self.canvas
    
    def place(self, height, width, x, y):
        self.canvas.height = height
        self.canvas.width  = width
        self.canvas.canvasx(x)
        self.canvas.canvasy(y)
    
    def unplace(self):
        
        
class TetrisLabel:
    def __init__(self,wrapped_root, &options):
        unwrapped_root =warpped_root.root
        self.label = tk.Label(unwrapped_root, &options)
        
    
    
class TetrisButton:
    def __init__(self, label, color):
        self.button = tk.Button()
        
        
        
class TetrisRect:
    def __init__(self, wrapped_canvas, a, b, c, d, color):
        upwrapped_canvas = wrapped_canvas.canvas
        self.rect = 
        

def mainLoop:
    tk.mainloop()
def 
        