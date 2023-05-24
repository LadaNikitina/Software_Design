from map import Map
from character import Character
import keyboard
# написать функцию рандомной генерации позиции по карте

m = Map()
m.generateMap()

# Создание объекта игрока
player = Character(0, 0)

# Обработчик нажатия клавиш
def handle_keypress(event):
    if event.name == 'up':
        player.move_up()
    elif event.name == 'down':
        player.move_down()
    elif event.name == 'left':
        player.move_left()
    elif event.name == 'right':
        player.move_right()

# Регистрация обработчика для нажатий клавиш
keyboard.on_press(handle_keypress)

# Программа будет работать до тех пор, пока не будет нажата клавиша Esc
keyboard.wait('esc')

# Вывод координат игрока после завершения программы
print(f"Player coordinates: ({player.coordX}, {player.coordY})")

m.drawMap()
print('\n')
m.drawPieceOfMap(centre_x=30, centre_y=24, height=20, width=20)

m = Map(mode=1)
m.generateMap()
m.drawMap()
print('\n')
m.drawPieceOfMap(centre_x=30, centre_y=24, height=20, width=20)
