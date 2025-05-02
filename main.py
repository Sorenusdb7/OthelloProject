import pygame
import sys
import math
from othpack import board
from othpack import headbar

pygame.init()
game_finish = False

screen = pygame.display.set_mode((600, 700))
game_board = board.Board(screen)
game_headbar = headbar.Headbar(screen)
#stuff
game_headbar.draw_headbar()
game_board.create_board()
game_board.draw_board()
pygame.display.update()

while game_finish == False:
    square_size = 600/8
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex = event.pos[0]
            column = math.floor(mousex/square_size)
            mousey = event.pos[1]
            row = math.floor((mousey - 100)/square_size)
            placed = game_board.place_piece(row, column)
            if placed==1:
                game_headbar.switch_turn()
                game_headbar.draw_headbar()
            if placed==2:
                game_headbar.switch_turn()
                game_headbar.draw_skipbar()
            if placed==3:
                winner = game_board.calc_winner()
                game_headbar.declare_winner(winner)
                game_finish = True
            game_board.draw_board()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            winner = game_board.calc_winner()
            game_headbar.declare_winner(winner)
            game_finish = True
    pygame.display.update()
while game_finish == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            sys.exit()
    pygame.display.update()