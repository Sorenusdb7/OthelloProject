import pygame
import sys
import math
from .square import Square

class Board:
    def __init__(self, WINDOW):
        self.WINDOW = WINDOW
        self.board = []
        self.square_list = []
        self.turn = 1
        self.skipped = 0
        self.turn_counter = 1

    def draw_board(self):
        square_size = 600/8
        for x in range(8):
            for y in range(8):
                pygame.draw.rect(self.WINDOW, (0, 0, 0), ((square_size * x), 
                                                                (100 + square_size * y), (square_size * (x+1)), (100 + square_size * (y+1))))
                pygame.draw.rect(self.WINDOW, (116, 159, 100), ((square_size * x + 3), 
                                                                (100 + square_size * y + 3), (square_size * (x+1) - 3), (100 + square_size * (y+1) - 3)))
        for square_row in self.square_list:
            for square in square_row:
                if square.get_side() == 1:
                    center = (square_size * square.get_x() + (square_size/2), square_size * square.get_y() + (square_size/2) + 100)
                    pygame.draw.circle(self.WINDOW, (0, 0, 0), center, (square_size/2 - 3))
                elif square.get_side() == 2:
                    center = (square_size * square.get_x() + (square_size/2), square_size * square.get_y() + (square_size/2) + 100)
                    pygame.draw.circle(self.WINDOW, (255, 255, 255), center, (square_size/2 - 3))
    
    def place_piece(self, row, col):
        square = self.square_list[col][row]
        occupied = square.get_side()
        print(occupied)
        if occupied == 0:
            square.set_side(self.turn)
            valid = self.check_place(square)
            if valid:
                self.skipped = 0
                self.check_flips(square)
                if self.turn == 1:
                    self.turn = 2
                else:
                    self.turn = 1
                if self.turn_counter == 60:
                    return 3
                self.turn_counter = self.turn_counter+1
                return 1
            else:
                square.set_side(0)
                if self.can_move() == 1:
                    return 0
                else:
                    if self.skipped == 0:
                        self.skipped = 1
                    else:
                        return 3
                    if self.turn == 1:
                        self.turn = 2
                    else:
                        self.turn = 1
                    return 2
        else:
            if self.can_move() == 1:
                return 0
            else:
                if self.skipped == 0:
                    self.skipped = 1
                else:
                    return 3
                if self.turn == 1:
                    self.turn = 2
                else:
                    self.turn = 1
                return 2
    
    def calc_winner(self):
        winner = 0
        for list in self.square_list:
            for square in list:
                if square.get_side() == 1:
                    winner = winner + 1
                elif square.get_side() == 2:
                    winner = winner - 1
        if winner > 1:
            winner = 1
        if winner < 0:
            winner = 2
        return winner
        
    def check_flips(self, square):
        print('side = ', square.get_side())
        for x in range(-1, 2):
            for y in range(-1, 2):
                captured = self.check_dir(square, square.get_side(), x, y)
                if captured:
                    #print(square.get_x(), ',', square.get_y())
                    #print(x, ',', y, ' captured')
                    self.flip_pieces(square, x, y)
                else: 
                    print(square.get_x(), ',', square.get_y())
                    print(x, ',', y, ' false')
    
    def check_place(self, square):
        valid = False
        for x in range(-1, 2):
            for y in range(-1, 2):
                captured = self.check_chain(square, square.get_side(), x, y, 0)
                if captured:
                    #print(square.get_x(), ',', square.get_y())
                    #print(x, ',', y, ' captured')
                    valid = True
        return valid

    
    def check_dir(self, square, originside, x, y):
        checkx = square.get_x() + x
        checky = square.get_y() + y
        if -1 < checkx < 8 and -1 < checky < 8:
            checksquare = self.square_list[checkx][checky]
            if originside == 1:
                if checksquare.get_side() == 2:
                    return self.check_dir(checksquare, originside, x, y)
                elif checksquare.get_side() == 1:
                    return True
                else:
                    return False
            elif originside == 2:
                if checksquare.get_side() == 1:
                    return self.check_dir(checksquare, originside, x, y)
                elif checksquare.get_side() == 2:
                    return True
                else:
                    return False
        else:
            return False
        
    def check_chain(self, square, originside, x, y, chain):
        checkx = square.get_x() + x
        checky = square.get_y() + y
        if -1 < checkx < 8 and -1 < checky < 8:
            checksquare = self.square_list[checkx][checky]
            if originside == 1:
                if checksquare.get_side() == 2:
                    return self.check_chain(checksquare, originside, x, y, chain+1)
                elif checksquare.get_side() == 1:
                    return chain
                else:
                    return 0
            elif originside == 2:
                if checksquare.get_side() == 1:
                    return self.check_chain(checksquare, originside, x, y, chain+1)
                elif checksquare.get_side() == 2:
                    return chain
                else:
                    return 0
        else:
            return 0
        
    def can_move(self):
        print("Checking for Move")
        for slist in self.square_list:
            for square in slist:
                if square.get_side() == 0:
                    print("checking a square")
                    square.set_side(self.turn)
                    valid = self.check_place(square)
                    square.set_side(0)
                    if valid:
                        print("Valid move for square ", square.get_x(), ", ", square.get_y())
                    if valid:
                        return 1
        return 0
        
    def flip_pieces(self, square, x, y):
        flipx = square.get_x() + x
        flipy = square.get_y() + y
        flipsquare = self.square_list[flipx][flipy]
        if flipsquare.get_side() != square.get_side():
            flipsquare.set_side(square.get_side())
            self.flip_pieces(flipsquare, x, y)
    
    def create_board(self):
        initializor = 0
        for x in range(8):
            square_row = []
            for y in range(8):
                new_square = Square(initializor, x, y)
                initializor = initializor + 1
                square_row.append(new_square)
            self.square_list.append(square_row)
        for x in range(3, 5):
            for y in range(3, 5):
                if x == y:
                    self.square_list[x][y].set_side(2)
                else:
                    self.square_list[x][y].set_side(1)