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
        self.cubes = [[Cube(self.my_grid[row][col], row, height, width, height)
                       for col in range(columns)] for row in range(rows)]

    def make_grid(self, win):
        space = self.width / 9
        for i in range(self.rows + 1):
            if i % 3 == 0 and i != 0:
                thickness = 4
            else:
                thickness = 1
            # draw row lines
            pygame.draw.line(win, (0, 0, 0), (0, space * i),
                             (self.width, space * i), thickness)
            # draw column lines
            pygame.draw.line(win, (0, 0, 0), (space * i, 0),
                             (space * i, self.height), thickness)

    def is_full(self):
        for row in range(self.rows):
            for col in range(self.columns):
                if self.cubes[row][col].value == 0:
                    return False
        return True


class Cube:
    rows = 9
    columns = 9

    def __init__(self, value, row, column, width, height):
        self.value = value
        self.row = row
        self.column = column
        self.width = width
        self.height = height
        self.temp_value = 0
        self.selected = False

    def make_cube(self, win):
        font = pygame.font.SysFont("comicsans", 40)
        space = self.width / 9

        x = self.column * space
        y = self.row * space

        # if existing value is 0 (for user to input)
        if self.temp_value != 0 and self.value == 0:
            text = font.render(str(self.temp_value), 1, (128, 128, 128))
            win.blit(text, (x+5, y+5))
        # if existing value is not 0 (fixed)
        elif self.value != 0:
            text = font.render(str(self.value), 1, (0, 0, 0))
            win.blit(text, (x + (space/2 - text.get_width()/2),
                            y + (space/2 - text.get_height()/2)))
        # outline cube with red when clicked
        if self.selected:
            pygame.draw.rect(win, (255, 0, 0), (x, y, space, space), 3)

    def set_value(self, value):
        self.value = value

    def set_temp_value(self, temp):
        self.temp_value = temp


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
