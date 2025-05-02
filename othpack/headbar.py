import pygame
import sys
import math

class Headbar:
    def __init__(self, WINDOW):
        self.WINDOW = WINDOW
        self.headbar = []
        self.turn = 0
        self.frame = (0, 0, 600, 100)

    def draw_headbar(self):
        if self.turn == 1:
            pygame.draw.rect(self.WINDOW, (255, 255, 255), self.frame)
            turn_font = pygame.font.SysFont('MyFont', 48)
            turn_text = turn_font.render('White turn. Press Enter to end game.', True, (0, 0, 0))
            self.WINDOW.blit(turn_text, (10, 40))
        elif self.turn == 0:
            pygame.draw.rect(self.WINDOW, (0, 0, 0), self.frame)
            turn_font = pygame.font.SysFont('MyFont', 48)
            turn_text = turn_font.render('Black turn. Press Enter to end game.', True, (255, 255, 255))
            self.WINDOW.blit(turn_text, (10, 40))
        return 0
    
    def draw_skipbar(self):
        if self.turn == 1:
            pygame.draw.rect(self.WINDOW, (255, 255, 255), self.frame)
            turn_font = pygame.font.SysFont('MyFont', 48)
            turn_text = turn_font.render('White turn. Black had no viable moves.', True, (0, 0, 0))
            self.WINDOW.blit(turn_text, (10, 40))
        elif self.turn == 0:
            pygame.draw.rect(self.WINDOW, (0, 0, 0), self.frame)
            turn_font = pygame.font.SysFont('MyFont', 48)
            turn_text = turn_font.render('Black turn. White had no viable moves.', True, (255, 255, 255))
            self.WINDOW.blit(turn_text, (10, 40))
        return 0
    
    def switch_turn(self):
        if self.turn == 1:
            self.turn = 0
        else:
            self.turn = 1
    
    def declare_winner(self, winner):
        if winner == 2:
            pygame.draw.rect(self.WINDOW, (255, 255, 255), self.frame)
            turn_font = pygame.font.SysFont('MyFont', 48)
            turn_text = turn_font.render('White wins. Press Enter to leave game.', True, (0, 0, 0))
            self.WINDOW.blit(turn_text, (10, 40))
        elif winner == 1:
            pygame.draw.rect(self.WINDOW, (0, 0, 0), self.frame)
            turn_font = pygame.font.SysFont('MyFont', 48)
            turn_text = turn_font.render('Black wins. Press Enter to leave game.', True, (255, 255, 255))
            self.WINDOW.blit(turn_text, (10, 40))
        else:
            pygame.draw.rect(self.WINDOW, (50, 50, 50), self.frame)
            turn_font = pygame.font.SysFont('MyFont', 48)
            turn_text = turn_font.render('Tie game. Press Enter to leave game.', True, (200, 200, 200))
            self.WINDOW.blit(turn_text, (10, 40))