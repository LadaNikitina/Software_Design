from map import Map
from character import Character
import keyboard
from os import system, name

# написать функцию рандомной генерации позиции по карте

m = Map()
m.generateMap()

# Создание объекта игрока
player = Character(m.height // 2, m.width // 2,)
m.drawPieceOfMap(centre_x=m.height // 2, centre_y=m.width // 2, height=20, width=20)


# Обработчик нажатия клавиш
def handle_keypress(event):
    if event.name == 'up':
        _ = system('cls')
        player.move_up()
        m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20)
    elif event.name == 'down':
        _ = system('cls')
        player.move_down()
        m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20)
    elif event.name == 'left':
        _ = system('cls')
        player.move_left()
        m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20)
    elif event.name == 'right':
        _ = system('cls')
        player.move_right()
        m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20)



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