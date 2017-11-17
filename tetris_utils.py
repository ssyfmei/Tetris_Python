# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 02:46:45 2017

@author: meixx115
"""

class Piece:
    def __init__(self, point_array, board):
        
        
        
        
class Board:
    def __init__(self, game):
        self.grid = self.
        
    
    def draw:
        
        
        
        
        
        
        
        
        
    
class Tetris:
    def __init__(self):
        self.root = tk.Tk()
        set_background()
        
        set_board()
        self.running = True
        key_bindings
        buttons
        run_game
    
    def set_background(self):
        self.root.title("Tetris")
        back = tk.Frame(self.root, width=205, height=605, bg='lightblue')
        back.pack()
    
    def setboard(self):
        
        self.root = tk.Tk()
        
         
        self.canvas = Canvas(root, 400, 200)
        self.board  = TetrisBoard(self)
        self.canvas.place(width=self.board.block_size * self.board.num_rows + 3,
                          height=self.board.block_size * self.board.num_columns + 6)
        self.board.draw()
    
    def key_bindings(self):
        self.root.bind()
        self.root.bind()
        self.root.bind()
        self.root.bind()
        
        
    def buttons(self):
        new_game = tk.Button(self.root, text='new game', width=9, height = 2,bg = 'lightcoral',   command=self.root.destroy)
        pause = tk.Button(self.root, text='pause',    width=6, height = 2,   bg = 'lightcoral',   command=self.root.destroy)
        quit1 = tk.Button(self.root, text='quit',     width=5, height = 2,   bg = 'lightcoral',   command=self.root.destroy)   
        move_left =tk.Button(self.root, text='left', width=6, height = 2,    bg = 'lightgreen',   command=self.root.destroy)
        move_right =tk.Button(self.root, text='right', width=6, height = 2,  bg = 'lightgreen',   command=self.root.destroy)
        rotate_clock =tk.Button(self.root, text='^_)', width=6, height = 2,  bg = 'lightgreen',   command=self.root.destroy)
        rotate_counter =tk.Button(self.root, text='(_^', width=6, height = 2,bg = 'lightgreen',   command=self.root.destroy)
        drop = tk.Button(self.root, text='drop', width=6, height = 2,        bg = 'lightgreen',   command=self.root.destroy)
        
        new_game.place(x=52, y=28, anchor="c")
        pause.place(x=115, y=28, anchor="c")
        quit1.place(x=163, y=28, anchor="c")
        rotate_counter.place(x=100, y=499, anchor="c")
        rotate_clock.place(x=100, y=581, anchor="c")
        move_left.place(x=48, y=540, anchor="c")
        move_right.place(x=152, y=540, anchor="c")
        drop.place(x=100, y=540, anchor="c")
        
        label = tk.Label(self.root, text="Current Score:", bg = 'lightblue')
        label.place(x=75, y=68, anchor="c")
        
    def draw_piece(piece, old = False):
        if old and piece.moved:
        end
        
        size = self.board.block_size
        blocks = piece.current_rotation
        start = piece.position
        
            
            
        
        
        