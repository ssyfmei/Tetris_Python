
import tkinter as tk
import random
import numpy
class Piece:               
    All_Colors = ['DarkGreen', 'dark blue', 'dark red', 'gold2', 'Purple3', 
               'OrangeRed2', 'LightSkyBlue']  
    def __init__(self, point_array, board):
        self.all_rotations = point_array
        self.rotation_index = random.choice(range(len(self.all_rotations)))
        self.color = random.choice(self.All_Colors)
        self.base_position = [5, 0]
        self.board = board
        self.moved = True
        self.All_Pieces = [[[[0, 0], [1, 0], [0, 1], [1, 1]]],    # square (only needs one)
               self.rotations([[0, 0], [-1, 0], [1, 0], [0, -1]]), # T
               [[[0, 0], [-1, 0], [1, 0], [2, 0]],       # long (only needs two)
               [[0, 0], [0, -1], [0, 1], [0, 2]]],
               self.rotations([[0, 0], [0, -1], [0, 1], [1, 1]]),   # L
               self.rotations([[0, 0], [0, -1], [0, 1], [-1, 1]]),  # inverted L
               self.rotations([[0, 0], [-1, 0], [0, -1], [1, -1]]), # S
               self.rotations([[0, 0], [1, 0], [0, -1], [-1, -1]])] # Z        
        
    def current_rotation(self):
        return self.all_rotations[self.rotation_index]
    def position(self):
        return self.base_position
    def color(self):
        return self.color
    def drop_by_one(self):
        self.moved = self.move(0, 1, 0)
        return self.moved
        
    def move(self, delta_x, delta_y, delta_rotation):
        moved = True
        potential = self.all_rotations[(self.rotation_index + delta_rotation) % len(self.all_rotations)]
        for posns in potential:
            if not (self.board.empty_at([posns[0] + delta_x + self.base_position[0],
                                         posns[1] + delta_y + self.base_position[1]])):
                return False
        if moved:
            self.base_position[0] += delta_x
            self.base_position[1] += delta_y
            self.rotation_index = (self.rotation_index + delta_rotation) % len(self.all_rotations)
        return moved
    
    def rotations(self, point_array):
        rotate1 = list(map(lambda x: [-x[1], x[0]], point_array))
        rotate2 = list(map(lambda x: [-x[0],-x[1]], point_array))
        rotate3 = list(map(lambda x: [ x[1],-x[0]], point_array))
        return [point_array, rotate1, rotate2, rotate3] 
    
    def next_piece(self, board): 
        return Piece(random.choice(self.All_Pieces), board)
        

        
class Board:
    def __init__(self, game):
        self.grid = [[None] * self.num_columns()] * self.num_rows()
        self.current_block = Piece([123],112).next_piece(self)
        self.current_pos = self.current_block.base_position
        self.score = 0
        self.game = game
        self.delay = 500
    
    def block_size(self):
        return 15
    
    def num_columns(self):
        return 10
    
    def num_rows(self):
        return 27
    def score(self):
        return self.score
        
    def delay(self):
        return self.delay
    
    def game_over(self):
        return len(list(filter(lambda x: x is not None, self.grid[0]))) > 0
        
    # Manipulate Blocks
    def run(self):
       ran = self.current_block.drop_by_one()
       if not ran:
           self.store_current()
           if (not self.game_over()):
               self.next_piece()
       self.game.update_score()
       self.draw()
           
        
    def move_left(self, event = None):
        if (not self.game_over()) and game.is_running():
            self.current_block.move(-1,0,0)
        self.draw()
    def move_right(self, event = None):
        if (not self.game_over()) and game.is_running():
            self.current_block.move(1,0,0)
        self.draw()
    def rotate_clockwise(self, event = None):
        if (not self.game_over()) and game.is_running():
            self.current_block.move(0,0,1)
        self.draw()
    def rotate_counter_clockwise(self, event = None):
        if (not self.game_over()) and game.is_running():
            self.current_block.move(0,0,-1)
        self.draw()
    
    def drop_all_the_way(self, event = None):
        if game.is_running():
            self.current_block.move(-1,0,0)
        self.draw()
        
    def next_piece(self):
        self.current_block = Piece([123],112).next_piece(self)
        self.current_pos   = self.current_block.base_position
    
    def store_current(self):
        self.location = self.current_block.current_rotation()
        displacement = self.current_block.position()
        for index in range(4):
            current = self.location[index]
            print(self.grid)
            self.grid[current[1]+displacement[1]][current[0]+displacement[0]] = 1#self.current_pos[index]
        #self.remove_filled()
        self.delay = max(self.delay - 2, 80)
        
    
    def empty_at(self, point):
        if (point[0] < 0 or point[0] >= self.num_columns()):
            return False
        elif (point[1] < 1):
            return True
        elif point[1] >= self.num_rows():
            return False
        return self.grid[point[1]][point[0]] is None
    
    def remove_filled(self):
        for num in range(2, len(self.grid)):
            #row = self.grid[num]
            if len(list(filter(lambda x: x is None, self.grid[num]))) == 0:
                #for item in self.grid[num]:
                #    item = None
                # move rows down
                for num2 in range(len(self.grid) - num + 1, len(self.grid) + 1):
                    self.grid[len(self.grid) - num2 + 1] = numpy.array(self.grid[len(self.grid) - num2 ])
                #insert new blank row at top
                self.grid[0] = numpy.array([None]* self.num_columns())
                # add score 
                self.score += 10
    def draw(self):
        self.current_pos = self.game.draw_piece(self.current_block, self.current_pos) 
    
    
    
class Tetris:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tetris")
        self.set_background()
        self.set_board()
        self.running = True
        self.key_bindings()
        self.buttons()
        self.run_game()
    
    def set_background(self):
        back = tk.Frame(self.root, width=205, height=605, bg='lightblue')
        back.pack()
    
    def set_board(self):
        self.board  = Board(self)
        #self.canvas = tk.Canvas(self.root, width= self.board.block_size() * self.board.num_rows() + 3, 
                                #height=self.board.block_size() * self.board.num_columns() + 6)
        
        #self.canvas.place(x=24,y=80, anchor="c")
        self.canvas = tk.Canvas(self.root, height=500, width=180)
        self.canvas.place(x=10,y=100)
        self.board.draw()
    
    def key_bindings(self):
        self.root.bind('n', self.new_game)
        self.root.bind('p', self.pause)
        self.root.bind('q', self.exitProgram)
        self.root.bind('a', self.board.move_left)
        self.root.bind('<Left>', self.board.move_left)
        
        self.root.bind('d', self.board.move_right)
        self.root.bind('<Right>',self.board.move_right)
        
        self.root.bind('s', self.board.rotate_clockwise)
        self.root.bind('<Down>', self.board.rotate_clockwise)
        
        self.root.bind('w', self.board.rotate_counter_clockwise)
        self.root.bind('<Up>', self.board.rotate_counter_clockwise)
        
        self.root.bind('space', self.board.drop_all_the_way)
        
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
        
        self.score = tk.Label(self.root, bg = 'lightblue')
        self.score['text'] = (self.board.score)
        self.score.place(x = 140, y = 68, anchor = "c")
        
    def new_game(self, event = None):
        self.canvas.delete("all")
        self.set_board()
        self.score.text(self.board.score)
        self.running = True
        self.run_game()
        
    def pause(self, event = None):
        if self.running:
            self.running = False
            ####
            # Timer
            ####
        else:
            self.running = True
            self.run_game()
            
    
    def update_score(self):
        self.score['text'] = self.board.score
    
    def run_game(self):
        self.board.run()
        self.root.after(self.board.delay, self.run_game)
        
    def is_running(self):
        return self.running
        
    # take a piece and old block list
    def draw_piece(self, piece, old = None):
        if old is not None and piece.moved:
            for block in old:
                self.canvas.delete(block)
        size = self.board.block_size()
        blocks = piece.current_rotation()
        start = piece.position()
        new_piece = []
        for block in blocks:
            new_piece.append(self.canvas.create_rectangle(start[0]*size + block[0]*size + 3, 
                       start[1]*size + block[1]*size,
                       start[0]*size + size + block[0]*size + 3, 
                       start[1]*size + size + block[1]*size, fill = piece.color))
        return new_piece
    def exitProgram(self, event=None):
        self.root.destroy()
            
        
game = Tetris()
game.root.mainloop()        
        