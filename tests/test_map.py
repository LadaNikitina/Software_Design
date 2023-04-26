import random
from field import WALL
from map import Map


# Проверяет, нет ли зон, куда нельзя зайти
def test():
    n = 20
    for i in range(n):
        print('Start', i)

        height = random.randrange(4, 100)
        width = random.randrange(4, 100)
        m = Map(height=height, width=width)
        m.generateMap()

        start = (0, 0)
        check = [[]]

        for h in range(height):
            check.append([])
            for w in range(width):
                check[h].append(False)
                if m.tiles[h][w] == WALL:
                    check[h][w] = True
                else:
                    start = (h, w)

        q = [start]
        while len(q) > 0:
            curr = q.pop(0)
            if curr[0] >= height or curr[0] < 0 or curr[1] >= width or curr[1] < 0:
                continue
            if check[curr[0]][curr[1]]:
                continue
            check[curr[0]][curr[1]] = True
            q.append((curr[0] - 1, curr[1]))
            q.append((curr[0] + 1, curr[1]))
            q.append((curr[0], curr[1] - 1))
            q.append((curr[0], curr[1] + 1))

        k = 0
        for h in range(height):
            for w in range(width):
                if check[h][w]:
                    k += 1

        if k != height * width:
            print()
            for h in range(height):
                for w in range(width):
                    p = ' '
                    if check[h][w]:
                        p = '█'
                    print(p, end='')
                print()
            print()
            m.drawMap()
        assert k == height * width

        print('Pass', i, 'from', n)
