import random
import sys

import numpy as np
import matplotlib.pyplot as plt
from field import NOTHING, WALL, PRICKLY_VINE, LAVA
from item import Poison, Artifact, Treasure

CHARACTER = '☺'
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
RED = [255, 0, 0]
GREEN = [0, 255, 0]
ORANGE = [255, 165, 0]
GREY = [169, 169, 169]


class Map:
    def __init__(self, height=60, width=100, p_prickly_vine=10, p_lava=10, k_poison=20, k_artifact=20, k_treasure=7, mode=0):
        self.height = height
        self.width = width
        self.p_prickly_vine = p_prickly_vine
        self.p_lava = p_lava
        self.k_poison = k_poison
        self.k_artifact = k_artifact
        self.k_treasure = k_treasure
        self.mode = mode

        self.tiles = [[]]
        self.items = {}
        self.itemsOnMap = []

    # Используется рандомизированный алгоритм Прима
    def generateMap(self):
        for h in range(self.height):
            self.tiles.append([])
            for w in range(self.width):
                self.tiles[h].append(WALL)
        x = random.randint(0, self.height // 2 - 1) * 2 + 1
        y = random.randint(0, self.width // 2 - 1) * 2 + 1
        self.tiles[x][y] = NOTHING
        to_check = []
        if y - 2 >= 0:
            to_check.append((x, y - 2))
        if y + 2 < self.width:
            to_check.append((x, y + 2))
        if x - 2 >= 0:
            to_check.append((x - 2, y))
        if x + 2 < self.height:
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
                    if y + 2 < self.width and self.tiles[x][y + 2] == NOTHING:
                        self.tiles[x][y + 1] = NOTHING
                        break
                elif d[dir_index] == 'EAST':
                    if x - 2 >= 0 and self.tiles[x - 2][y] == NOTHING:
                        self.tiles[x - 1][y] = NOTHING
                        break
                elif d[dir_index] == 'WEST':
                    if x + 2 < self.height and self.tiles[x + 2][y] == NOTHING:
                        self.tiles[x + 1][y] = NOTHING
                        break
                d.pop(dir_index)

            if y - 2 >= 0 and self.tiles[x][y - 2] == WALL:
                to_check.append((x, y - 2))
            if y + 2 < self.width and self.tiles[x][y + 2] == WALL:
                to_check.append((x, y + 2))
            if x - 2 >= 0 and self.tiles[x - 2][y] == WALL:
                to_check.append((x - 2, y))
            if x + 2 < self.height and self.tiles[x + 2][y] == WALL:
                to_check.append((x + 2, y))

        for h in range(self.height - 1):
            if h == 0:
                continue
            for w in range(self.width - 1):
                if w == 0:
                    continue
                if self.tiles[h][w] == WALL \
                        and self.tiles[h][w - 1] == NOTHING \
                        and self.tiles[h - 1][w] == NOTHING \
                        and self.tiles[h][w + 1] == NOTHING \
                        and self.tiles[h + 1][w] == NOTHING:
                    self.tiles[h][w] = NOTHING

        for i in range(4):
            dead_ends = []
            for h in range(self.height):
                for w in range(self.width):
                    if self.tiles[h][w] == NOTHING:
                        neighbors = 0
                        if h - 1 >= 0 and self.tiles[h - 1][w] == NOTHING:
                            neighbors += 1
                        if h + 1 < self.height and self.tiles[h + 1][w] == NOTHING:
                            neighbors += 1
                        if w - 1 >= 0 and self.tiles[h][w - 1] == NOTHING:
                            neighbors += 1
                        if w + 1 < self.width and self.tiles[h][w + 1] == NOTHING:
                            neighbors += 1
                        if neighbors <= 1:
                            dead_ends.append((h, w))
            for cell in dead_ends:
                self.tiles[cell[0]][cell[1]] = WALL
        # Здесь заканчивается генерация стен

        # Внешние границы делаем стенами
        for w in range(self.width):
            self.tiles[0][w] = WALL
            self.tiles[self.height - 1][w] = WALL
        for h in range(self.height):
            self.tiles[h][0] = WALL
            self.tiles[h][self.width - 1] = WALL

        # С заданной вероятностью генерируем ловушки: колючие лозы и лаву
        for h in range(self.height):
            for w in range(self.width):
                if self.tiles[h][w] != NOTHING:
                    continue
                if random.randint(0, 100) <= self.p_prickly_vine:
                    self.tiles[h][w] = PRICKLY_VINE
                elif random.randint(0, 100) <= self.p_lava:
                    self.tiles[h][w] = LAVA

        # Генерируем вещи
        while self.k_poison > 0:
            h = random.randint(0, self.height-1)
            w = random.randint(0, self.width-1)
            if self.tiles[h][w] == WALL:
                continue
            poison = Poison(h, w)
            self.items[(h, w)] = poison
            self.itemsOnMap.append(poison)
            self.k_poison -= 1
        while self.k_artifact > 0:
            h = random.randint(0, self.height-1)
            w = random.randint(0, self.width-1)
            if self.tiles[h][w] == WALL:
                continue
            artifact = Artifact(h, w)
            self.items[(h, w)] = artifact
            self.itemsOnMap.append(artifact)
            self.k_artifact -= 1
        while self.k_treasure > 0:
            h = random.randint(0, self.height-1)
            w = random.randint(0, self.width-1)
            if self.tiles[h][w] == WALL:
                continue
            treasure = Treasure(h, w)
            self.items[(h, w)] = treasure
            self.itemsOnMap.append(treasure)
            self.k_treasure -= 1

    def getField(self, x, y):
        return self.tiles[x][y]

    def drawMap(self):
        self.drawPieceOfMap(centre_x=self.height // 2, centre_y=self.width // 2, height=self.height, width=self.width)

    # mode = 0 -- простая отрисовка в консили символами
    # mode = 1 -- отрисовка цветными квадратиками
    def drawPieceOfMap(self, centre_x, centre_y, height, width, mode=-1):
        if mode == -1:
            mode = self.mode

        shift_x = centre_x - height // 2
        shift_y = centre_y - width // 2

        if mode == 0:
            for h in range(height):
                for w in range(width):
                    if w + shift_y >= self.width or h + shift_x >= self.height or w + shift_y < 0 or h + shift_x < 0:
                        print(' ', end='')
                    elif h + shift_x == centre_x and w + shift_y == centre_y:
                        if self.tiles[h + shift_x][w + shift_y] != WALL:
                            print(CHARACTER, end='')
                        else:
                            print("There can't be a hero in the center because there is a wall here!", file=sys.stderr)
                            print(self.tiles[h + shift_x][w + shift_y].fieldSymbol, end='')
                    elif (h + shift_x, w + shift_y) in self.items:
                        print(self.items[(h + shift_x, w + shift_y)].fieldSymbol, end='')
                    else:
                        print(self.tiles[h + shift_x][w + shift_y].fieldSymbol, end='')
                print()
            return
        if mode == 1:
            map_color = np.zeros((height, width, 3))
            for h in range(height):
                for w in range(width):
                    if w + shift_y >= self.width or h + shift_x >= self.height or w + shift_y < 0 or h + shift_x < 0:
                        map_color[h][w] = WHITE
                    elif h + shift_x == centre_x and w + shift_y == centre_y:
                        if self.tiles[h + shift_x][w + shift_y] != WALL:
                            map_color[h][w] = ORANGE
                        else:
                            print("There can't be a hero in the center because there is a wall here!", file=sys.stderr)
                            map_color[h][w] = BLACK
                    elif (h + shift_x, w + shift_y) in self.items:
                        map_color[h][w] = GREY
                    elif self.tiles[h + shift_x][w + shift_y] == NOTHING:
                        map_color[h][w] = WHITE
                    elif self.tiles[h + shift_x][w + shift_y] == WALL:
                        map_color[h][w] = BLACK
                    elif self.tiles[h + shift_x][w + shift_y] == PRICKLY_VINE:
                        map_color[h][w] = GREEN
                    elif self.tiles[h + shift_x][w + shift_y] == LAVA:
                        map_color[h][w] = RED
            plt.imshow(map_color)
            ax = plt.gca()
            ax.axes.xaxis.set_visible(False)
            ax.axes.yaxis.set_visible(False)
            plt.show()
            return
