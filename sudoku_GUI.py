import pygame
from sudoku import solve, check_valid
import time
pygame.font.init()


class Grid:
    my_grid = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    def __init__(self, rows, columns, width, height):
        self.rows = rows
        self.columns = columns
        self.width = width
        self.height = height

    def make_grid(self, win):
        space = self.width / 9
        for i in range(self.rows + 1):
            if i % 3 == 0 and i != 0:
                thickness = 4
            else:
                thickness = 1
            pygame.draw.line(win, (0, 0, 0), (0, space * i),
                             (self.width, space * i), thickness)
            pygame.draw.line(win, (0, 0, 0), (space * i, 0),
                             (space * i, self.height), thickness)


class Cube:
    rows = 9
    columns = 9

    def __init__(self, value, row, columns, width, height):
        self.value = value
        self.row = row
        self.columns = columns
        self.width = width
        self.height = height
        self.temp_value = 0


def redraw_window(win, board):
    win.fill((255, 255, 255))
    board.make_grid(win)


def main():
    win = pygame.display.set_mode((540, 600))
    pygame.display.set_caption("Sudoku")
    board = Grid(9, 9, 540, 540)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        redraw_window(win, board)
        pygame.display.update()


main()
pygame.quit()
