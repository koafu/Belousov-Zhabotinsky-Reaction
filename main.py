import pygame
from cell import Cell
import random
import time

class Reaction:

    def __init__(self):
        pygame.init()
        self.width = 200
        self.height = 200
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Belousov Reaction")
        self.clock = pygame.time.Clock()
        self.ticks = 60
        self.exit = False

        self.q = random.randint(2, 255)
        self.k1 = random.randint(1,8)
        self.k2 = random.randint(1,8)
        self.g = random.randint(1,100)

        self.grid = [[] for n in range(self.width)]
        for x in range(self.width):
            for y in range(self.height):
                state = random.randint(1, self.q + 1)
                self.grid[x].append(Cell(x, y, state))

    def update_window(self, pxarray):
        for x in range(self.width):
            for y in range(self.height):
                color = self.translate(self.grid[x][y].state, 1, self.q, 1, 255)
                pxarray[x,y] = int(color), int(color), int(color)

    def next_generation(self):
        for cols in self.grid:
            for cell in cols:
                cell.check_neighbors(self.grid, self.q, self.g, self.k1, self.k2)

        for cols in self.grid:
            for cell in cols:
                if cell.state == self.q:
                    cell.state = 1
                elif cell.state == 1:
                    cell.state = cell.info['v']
                else:
                    cell.state = cell.info['vi']

                if cell.state > self.q:
                    cell.state = self.q

    def translate(self, value, leftMin, leftMax, rightMin, rightMax):
        # Figure out how 'wide' each range is
        leftSpan = leftMax - leftMin
        rightSpan = rightMax - rightMin

        # Convert the left range into a 0-1 range (float)
        valueScaled = float(value - leftMin) / float(leftSpan)

        # Convert the 0-1 range into a value in the right range.
        return rightMin + (valueScaled * rightSpan)

    def run(self):

        pxarray = pygame.PixelArray(self.screen)
        print("q: {}, k1: {}, k2: {}, g: {}".format(self.q, self.k1, self.k2, self.g))
        while not self.exit:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True

            self.screen.fill((255,255,255))

            self.next_generation()
            self.update_window(pxarray)

            pygame.display.flip()
            self.clock.tick(self.ticks)

        pygame.quit()

if __name__ == '__main__':
    reaction = Reaction()
    reaction.run()
