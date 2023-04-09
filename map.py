import random
import numpy as np
import matplotlib.pyplot as plt

WALL = '█'
NOTHING = ' '


class Map:
    def __init__(self):
        self.height = 60
        self.width = 60
        self.tiles = [[]]
        self.itemsOnMap = []

    def generateMap(self):
        for w in range(self.width):
            self.tiles.append([])
            for h in range(self.height):
                self.tiles[w].append(WALL)
        x = random.randint(0, self.width // 2 - 1) * 2 + 1
        y = random.randint(0, self.height // 2 - 1) * 2 + 1
        self.tiles[x][y] = NOTHING
        to_check = []
        if y - 2 >= 0:
            to_check.append((x, y - 2))
        if y + 2 < self.height:
            to_check.append((x, y + 2))
        if x - 2 >= 0:
            to_check.append((x - 2, y))
        if x + 2 < self.width:
            to_check.append((x + 2, y))

        while len(to_check) > 0:
            index = random.randint(0, len(to_check) - 1)
            cell = to_check[index]
            x = cell[0]
            y = cell[1]
            self.tiles[x][y] = NOTHING
            to_check.pop(index)

            d = ['NORTH', 'SOUTH', 'EAST', 'WEST']
            while len(d) > 0:
                dir_index = random.randint(0, len(d) - 1)
                if d[dir_index] == 'NORTH':
                    if y - 2 >= 0 and self.tiles[x][y - 2] == NOTHING:
                        self.tiles[x][y - 1] = NOTHING
                        break
                elif d[dir_index] == 'SOUTH':
                    if y + 2 < self.height and self.tiles[x][y + 2] == NOTHING:
                        self.tiles[x][y + 1] = NOTHING
                        break
                elif d[dir_index] == 'EAST':
                    if x - 2 >= 0 and self.tiles[x - 2][y] == NOTHING:
                        self.tiles[x - 1][y] = NOTHING
                        break
                elif d[dir_index] == 'WEST':
                    if x + 2 < self.width and self.tiles[x + 2][y] == NOTHING:
                        self.tiles[x + 1][y] = NOTHING
                        break
                d.pop(dir_index)

            if y - 2 >= 0 and self.tiles[x][y - 2] == WALL:
                to_check.append((x, y - 2))
            if y + 2 < self.height and self.tiles[x][y + 2] == WALL:
                to_check.append((x, y + 2))
            if x - 2 >= 0 and self.tiles[x - 2][y] == WALL:
                to_check.append((x - 2, y))
            if x + 2 < self.width and self.tiles[x + 2][y] == WALL:
                to_check.append((x + 2, y))

        for w in range(self.width - 1):
            if w == 0:
                continue
            for h in range(self.height - 1):
                if h == 0:
                    continue
                if self.tiles[w][h] == WALL and self.tiles[w - 1][h] == NOTHING and self.tiles[w][h - 1] == NOTHING and \
                        self.tiles[w + 1][h] == NOTHING and self.tiles[w][h + 1] == NOTHING:
                    self.tiles[w][h] = NOTHING

        for i in range(4):
            dead_ends = []
            for h in range(self.height):
                for w in range(self.width):
                    if self.tiles[w][h] == NOTHING:
                        neighbors = 0
                        if h - 1 >= 0 and self.tiles[w][h - 1] == NOTHING:
                            neighbors += 1
                        if h + 1 < self.height and self.tiles[w][h + 1] == NOTHING:
                            neighbors += 1
                        if w - 1 >= 0 and self.tiles[w - 1][h] == NOTHING:
                            neighbors += 1
                        if w + 1 < self.width and self.tiles[w + 1][h] == NOTHING:
                            neighbors += 1
                        if neighbors <= 1:
                            dead_ends.append((w, h))
            for cell in dead_ends:
                self.tiles[cell[0]][cell[1]] = WALL

        for w in range(self.width):
            self.tiles[w][0] = WALL
            self.tiles[w][self.height - 1] = WALL
        for h in range(self.height):
            self.tiles[0][h] = WALL
            self.tiles[self.width - 1][h] = WALL

    def getField(self, x, y):
        return self.tiles[x][y]

    def drawMap(self):
        res = np.zeros((self.height, self.height, 3))
        for h in range(self.height):
            for w in range(self.width):
                if self.tiles[w][h] == NOTHING:
                    res[w][h] = [255, 255, 255]
        plt.imshow(res)
        ax = plt.gca()
        ax.axes.xaxis.set_visible(False)
        ax.axes.yaxis.set_visible(False)
        plt.show()
