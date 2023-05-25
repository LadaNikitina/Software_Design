import random
import sys

import numpy as np
import matplotlib.pyplot as plt

from enemy import make_mummy, make_grasshopper, make_lost_traveler
from field import NOTHING, WALL, PRICKLY_VINE, LAVA
from item import Poison, Artifact, Treasure
from os import system, name

CHARACTER = 'I'
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
RED = [255, 0, 0]
GREEN = [0, 255, 0]
ORANGE = [255, 165, 0]
BLUE = [0, 0, 255]
PURPLE = [139, 0, 255]


class Map:
    # Вероятности для врагов должны отличаться в зависимости от уровня, см. описание в hw8
    def __init__(self, height=60, width=100, p_prickly_vine=10, p_lava=10, p_mummy=0, p_grasshopper=0, p_lost_traveler=0, k_poison=20, k_artifact=20, k_treasure=7, mode=0):
        height = max(height, 4)
        width = max(width, 4)
        p_prickly_vine = max(p_prickly_vine, 0)
        p_lava = max(p_lava, 0)
        p_mummy = max(p_mummy, 0)
        p_grasshopper = max(p_grasshopper, 0)
        p_lost_traveler = max(p_lost_traveler, 0)
        k_poison = max(k_poison, 0)
        k_artifact = max(k_artifact, 0)
        k_treasure = max(k_treasure, 1)

        self.height = height
        self.width = width
        self.p_prickly_vine = p_prickly_vine
        self.p_lava = p_lava
        self.p_mummy = p_mummy
        self.p_grasshopper = p_grasshopper
        self.p_lost_traveler = p_lost_traveler
        self.k_poison = k_poison
        self.k_artifact = k_artifact
        self.k_treasure = k_treasure
        self.mode = mode

        self.tiles = []
        self.items = {}
        self.itemsOnMap = []
        self.enemy = [] # Не словарь, потому что будут перемещаться часто, так что просто отрисовываю поверх всех ловушек

    # Используется рандомизированный алгоритм Прима
    def generateMap(self):
        self.height -= 2
        self.width -= 2

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
            cell = to_check.pop(index)
            x = cell[0]
            y = cell[1]
            self.tiles[x][y] = NOTHING

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

        # Добавляем внешние границы -- стены
        up = []
        down = []
        for w in range(self.width):
            up.append(WALL)
            down.append(WALL)
        self.tiles = [up] + self.tiles + [down]
        self.height += 2
        for h in range(self.height):
            self.tiles[h] = [WALL] + self.tiles[h] + [WALL]
        self.width += 2

        # С заданной вероятностью генерируем ловушки: колючие лозы и лаву
        for h in range(self.height):
            for w in range(self.width):
                if self.tiles[h][w] != NOTHING:
                    continue
                if random.randint(0, 100) <= self.p_prickly_vine:
                    self.tiles[h][w] = PRICKLY_VINE
                elif random.randint(0, 100) <= self.p_lava:
                    self.tiles[h][w] = LAVA

        # С заданной вероятностью генерируем врагов: мумий, кузнечиков и заплутавших путников
        # Они могут стоять на одной клетке с ловушками и вещами
        for h in range(self.height):
            for w in range(self.width):
                if self.tiles[h][w] == WALL:
                    continue
                if random.randint(0, 100) <= self.p_mummy:
                    self.enemy.append(make_mummy(h, w))
                elif random.randint(0, 100) <= self.p_grasshopper:
                    self.enemy.append(make_grasshopper(h, w))
                elif random.randint(0, 100) <= self.p_lost_traveler:
                    self.enemy.append(make_lost_traveler(h, w))

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
    def drawPieceOfMap(self, centre_x, centre_y, height, width, health, time, mode=-1):
        if mode == -1:
            mode = self.mode

        shift_x = centre_x - height // 2
        shift_y = centre_y - width // 2

        tiles_and_enemy = []
        for h in range(self.height):
            tiles_and_enemy.append([])
            for w in range(self.width):
                tiles_and_enemy[h].append(self.tiles[h][w].fieldSymbol)
        for e in self.enemy:
            tiles_and_enemy[e.coordX][e.coordY] = e.symbol

        if mode == 0:
            if tiles_and_enemy[centre_x][centre_y] == WALL.fieldSymbol:
                return 1
            _ = system('cls')
            for h in range(height):
                for w in range(width):
                    if w + shift_y >= self.width or h + shift_x >= self.height or w + shift_y < 0 or h + shift_x < 0:
                        print(' ', end='')
                    elif h + shift_x == centre_x and w + shift_y == centre_y:
                        if tiles_and_enemy[h + shift_x][w + shift_y] != WALL.fieldSymbol:
                            print(CHARACTER, end='')
                        else:
                            print("There can't be a hero in the center because there is a wall here!", file=sys.stderr)
                            print(tiles_and_enemy[h + shift_x][w + shift_y], end='')
                    elif (h + shift_x, w + shift_y) in self.items:
                        print(self.items[(h + shift_x, w + shift_y)].fieldSymbol, end='')
                    else:
                        print(tiles_and_enemy[h + shift_x][w + shift_y], end='')
                print()
            print(f"HEALTH SCORE: {health}")
            print(f"TIME LEFT: {time}")
            return 0
        if mode == 1:
            map_color = np.zeros((height, width, 3))
            for h in range(height):
                for w in range(width):
                    if w + shift_y >= self.width or h + shift_x >= self.height or w + shift_y < 0 or h + shift_x < 0:
                        map_color[h][w] = WHITE
                    elif h + shift_x == centre_x and w + shift_y == centre_y:
                        if tiles_and_enemy[h + shift_x][w + shift_y] != WALL.fieldSymbol:
                            map_color[h][w] = BLUE
                        else:
                            print("There can't be a hero in the center because there is a wall here!", file=sys.stderr)
                            map_color[h][w] = BLACK
                    elif (h + shift_x, w + shift_y) in self.items:
                        map_color[h][w] = ORANGE
                    elif tiles_and_enemy[h + shift_x][w + shift_y] == NOTHING.fieldSymbol:
                        map_color[h][w] = WHITE
                    elif tiles_and_enemy[h + shift_x][w + shift_y] == WALL.fieldSymbol:
                        map_color[h][w] = BLACK
                    elif tiles_and_enemy[h + shift_x][w + shift_y] == PRICKLY_VINE.fieldSymbol:
                        map_color[h][w] = GREEN
                    elif tiles_and_enemy[h + shift_x][w + shift_y] == LAVA.fieldSymbol:
                        map_color[h][w] = RED
                    else: # Это враги
                        map_color[h][w] = PURPLE
            plt.imshow(map_color)
            ax = plt.gca()
            ax.axes.xaxis.set_visible(False)
            ax.axes.yaxis.set_visible(False)
            plt.show()
            return 0
