from map import Map
from character import Character
import keyboard

# написать функцию рандомной генерации позиции по карте

m = Map()
m.generateMap()

# Создание объекта игрока
player = Character(m.height // 2, m.width // 2)
m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20)

# Обработчик нажатия клавиш
def handle_keypress(event):
    if event.name == 'up':
        player.move_up()
        result = m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20)
        if result == 1:
            player.move_down()
        else:
            print("Player health:", player.health)
    elif event.name == 'down':
        player.move_down()
        result = m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20)
        if result == 1:
            player.move_up()
        else:
            print("Player health:", player.health)
    elif event.name == 'left':
        player.move_left()
        result = m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20)
        if result == 1:
            player.move_right()
        else:
            print("Player health:", player.health)
    elif event.name == 'right':
        player.move_right()
        result = m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20)
        if result == 1:
            player.move_left()
        else:
            print("Player health:", player.health)

# Регистрация обработчика для нажатий клавиш
keyboard.on_press(handle_keypress)

# Программа будет работать до тех пор, пока не будет нажата клавиша Esc
keyboard.wait('esc')

# Вывод координат игрока после завершения программы
print(f"Player coordinates: ({player.coordX}, {player.coordY})")
#
# m.drawMap()
# print('\n')
# m.drawPieceOfMap(centre_x=30, centre_y=24, height=20, width=20)