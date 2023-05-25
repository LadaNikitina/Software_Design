from map import Map
from character import Character
import keyboard
import time

def main():
    # написать функцию рандомной генерации позиции по карте

    # Добавление таймера для игры
    TIMELIMIT = 15  # seconds #TODO добавить логику выбора таймлимита при старте уровня
    START = time.time()
    END = START + TIMELIMIT

    m = Map()
    m.generateMap()

    # Создание объекта игрока
    player = Character(m.height // 2, m.width // 2)
    m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20, health=player.health, time=TIMELIMIT)

    TIMEOVER = False

    while True:
        time_left = int(END - time.time())
        if time_left <= 0:
            TIMEOVER = True
            break

        key = keyboard.read_key() # клавиша, нажатая игроком

        if key == 'esc': # выход из игры
            break

        if key == 'up':
            player.move_up()
            result = m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20, health=player.health, time=time_left)
            if result == 1:
                player.move_down()
            continue

        if key == 'down':
            player.move_down()
            result = m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20, health=player.health, time=time_left)
            if result == 1:
                player.move_up()
            continue

        if key == 'left':
            player.move_left()
            result = m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20, health=player.health, time=time_left)
            if result == 1:
                player.move_right()
            continue

        if key == 'right':
            player.move_right()
            result = m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20, health=player.health, time=time_left)
            if result == 1:
                player.move_left()
            continue

    if TIMEOVER:
        print("- - - \nTIME IS UP! You didn't escape the tombs so you became Tutankhamun's eternal slave.\n- - - \nGAME OVER\n- - -")
    # Вывод координат игрока после завершения программы
    #print(f"Player coordinates: ({player.coordX}, {player.coordY})")
    #
    # m.drawMap()
    # print('\n')
    # m.drawPieceOfMap(centre_x=30, centre_y=24, height=20, width=20)

if __name__=="__main__":
    main()