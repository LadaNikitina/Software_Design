from map import Map
from character import Character
import keyboard
import time

def main():
    # написать функцию рандомной генерации позиции по карте

    m = Map()
    m.generateMap()

    # Создание объекта игрока
    player = Character(m.height // 2, m.width // 2)
    m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20)

    # Добавление таймера для игры
    TIMELIMIT = 2 * 60  # seconds #TODO добавить логику выбора таймлимита при старте уровня
    START = time.time()
    END = START + TIMELIMIT

    while True:
        key = keyboard.read_key() # клавиша, нажатая игроком

        if key == 'esc': # выход из игры
            break

        if time.time() >= END: # кончилось время
            break

        if key == 'up':
            player.move_up()
            result = m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20)
            if result == 1:
                player.move_down()
            else:
                print("Player health:", player.health)
            continue

        if key == 'down':
            player.move_down()
            result = m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20)
            if result == 1:
                player.move_up()
            else:
                print("Player health:", player.health)
            continue

        if key == 'left':
            player.move_left()
            result = m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20)
            if result == 1:
                player.move_right()
            else:
                print("Player health:", player.health)
            continue

        if key == 'right':
            player.move_right()
            result = m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20)
            if result == 1:
                player.move_left()
            else:
                print("Player health:", player.health)
            continue

    print("- - - \nGAME OVER\n- - -")
    # Вывод координат игрока после завершения программы
    #print(f"Player coordinates: ({player.coordX}, {player.coordY})")
    #
    # m.drawMap()
    # print('\n')
    # m.drawPieceOfMap(centre_x=30, centre_y=24, height=20, width=20)

if __name__=="__main__":
    main()