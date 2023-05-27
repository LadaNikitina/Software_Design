from map import Map
from character import Character
import keyboard
import time
from field import PRICKLY_VINE, LAVA


def main():
    # написать функцию рандомной генерации позиции по карте

    # Добавление таймера для игры
    TIMELIMIT = 60  # seconds #TODO добавить логику выбора таймлимита при старте уровня
    START = time.time()
    END = START + TIMELIMIT

    m = Map()
    m.generateMap()

    # Создание объекта игрока
    player = Character(m.height // 2, m.width // 2)
    m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20, time=TIMELIMIT, player=player)

    TIMEOVER = False
    SUCCESS = False
    DEAD = False

    while True:
        time.sleep(0.3)
        time_left = int(END - time.time())
        if time_left <= 0:
            TIMEOVER = True
            break
        if player.treasures >= 5:
            SUCCESS = True
            break
        if player.health <= 0:
            DEAD = True
            break

        key = keyboard.read_key()  # клавиша, нажатая игроком

        if key == 'esc':  # выход из игры
            break

        if key == 'up':
            player.move_up()
            result = m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20,
                                      time=time_left, player=player)
            if result == 1:
                player.move_down()
            continue

        if key == 'down':
            player.move_down()
            result = m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20,
                                      time=time_left, player=player)
            if result == 1:
                player.move_up()
            continue

        if key == 'left':
            player.move_left()
            result = m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20,
                                      time=time_left, player=player)
            if result == 1:
                player.move_right()
            continue

        if key == 'right':
            player.move_right()
            result = m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20,
                                      time=time_left, player=player)
            if result == 1:
                player.move_left()
            continue

        if key == 'p':  # взять зелье/артефакт/сокровище и положить в инвентарь
            pass
        if key == 'b':  # взять первый предмет из рюкзака
            pass
        if key == 'q':  # использовать предмет
            pass
        if key == 'r':  # убрать артефакт с себя в инвентарь
            pass

        field = m.getField(player.coordX, player.coordY)
        if field.fieldSymbol == PRICKLY_VINE.fieldSymbol or field.fieldSymbol == LAVA.fieldSymbol:  # TODO запустить с дебаггером
            player.set_health(player.health - 5)


    if DEAD:
        print("- - - \nOh, no... You are dead...\n- - - \nGAME OVER\n- - -")

    if TIMEOVER:
        print(
            "- - - \nTIME IS UP! You didn't escape the tombs so you became Tutankhamun's eternal slave.\n- - - \nGAME OVER\n- - -")

    if SUCCESS:
        print("- - - \n MISSION COMPLETED! You've collected all treasures! See you in the next tomb ;)\n- - -")


if __name__ == "__main__":
    main()
