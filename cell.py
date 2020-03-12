import pygame
import random

class Cell:

    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state

    def __repr__(self):
        return 'Cell({})'.format(self.state)

    def show(self, screen, q):
        pass

    def get_neighbors(self, grid):
        neighbors = []
        for x in range(-1, 2, 1):
            for y in range(-1, 2, 1):
                try:
                    if grid[self.x + x][self.y + y] == self:
                        continue
                    neighbors.append(grid[self.x + x][self.y + y])

                except IndexError:
                    continue

        return neighbors

    def check_neighbors(self, grid, q, g, k1, k2):
        self.info = {}
        neighbors = self.get_neighbors(grid)

        a = 0
        b = 0
        for cell in neighbors:
            if cell.state >= 2 and cell.state < q:
                a += 1
            if cell.state == q:
                b += 1
        self.info['v'] = a/k1 + b/k2 + 1

        c = 0
        S = self.state
        for cell in neighbors:
            S += cell.state
            if cell.state == 1:
                c += 1
        self.info['vi'] = S / (9-c) + g
