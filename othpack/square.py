import pygame
import sys
import math

class Square:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.side = 0
    
    def get_side(self):
        return self.side
    
    def set_side(self, side):
        self.side = side
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y