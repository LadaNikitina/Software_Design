from map import Map
from character import Character
import keyboard
import time
from field import PRICKLY_VINE, LAVA
from item import Potion, Artifact, Treasure
from item import PotionType, ArtifactType


def main():
    # написать функцию рандомной генерации позиции по карте

    # Добавление таймера для игры
    TIMELIMIT = 2 * 60  # seconds #TODO добавить логику выбора таймлимита при старте уровня
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

    item_ind = 0 # для итерации по объектам рюкзака

    while True:
        time.sleep(0.3)
        time_left = int(END - time.time())
        if time_left <= 0:
            m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20, time=0, player=player)
            TIMEOVER = True
            break
        if player.treasures == m.treasures_count:
            SUCCESS = True
            break
        if player.health <= 0:
            m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20, time=time_left,
                             player=player)
            DEAD = True
            break

        key = keyboard.read_key()  # клавиша, нажатая игроком

        if key == 'esc':  # выход из игры
            break
        elif key == 'up':
            player.move_up()
            result = m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20,
                                      time=time_left, player=player)
            if result == 1:
                player.move_down()
        elif key == 'down':
            player.move_down()
            result = m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20,
                                      time=time_left, player=player)
            if result == 1:
                player.move_up()
        elif key == 'left':
            player.move_left()
            result = m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20,
                                      time=time_left, player=player)
            if result == 1:
                player.move_right()
        elif key == 'right':
            player.move_right()
            result = m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20,
                                      time=time_left, player=player)
            if result == 1:
                player.move_left()
        elif key == 'enter': # берем найденную вещь и кладем в рюкзак
            if (player.coordX, player.coordY) in m.items:
                if isinstance(item, Treasure):
                    player.treasures += 1
                else:
                    item = m.items[(player.coordX, player.coordY)]
                    player.items.append(item)
                m.items.pop((player.coordX, player.coordY))
                m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20,
                                 time=time_left, player=player)
        elif key == '0':
            if len(player.items) == 0:
                message = "Backpack is empty."
                m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20,
                                 time=time_left, player=player, message=message)
            else:
                item_ind = 0
                item = player.items[item_ind]
                message = str.upper(item.name)+ ": " + item.descr + "\nPress 1 to see the next item.\n" \
                                                                    "Press 2 to use the item.\n" \
                                                                    "Press any other key to close the backpack"
                m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20,
                                 time=time_left, player=player, message=message)
        elif key == '1':
            item_ind += 1
            if item_ind >= len(player.items):
                item_ind = 0
            item = player.items[item_ind]
            message = str.upper(item.name) + ": " + item.descr + "\nPress 1 to see the next item.\n" \
                                                                    "Press 2 to use the item.\n" \
                                                                    "Press any other key to close the backpack"
            m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20,
                             time=time_left, player=player, message=message)
        elif key == '2':
            while item_ind >= len(player.items):
                item_ind - len(player.items)
            if isinstance(item, Artifact) and player.artifact is not None:
                m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20,
                                 time=time_left, player=player, message="You can use only one artifact at the same time.")
                continue
            item = player.items[item_ind]
            item.applyToCharacter(player)
            player.items.pop(item_ind)
            item_ind = 0
            if isinstance(item, Artifact):
                player.artifact = item
            m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20,
                             time=time_left, player=player, message="Item was used successfully")
        elif key == '3':
            if player.artifact is not None:
                player.artifact.returnToInventory(player)
                player.artifact = None
                m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20,
                             time=time_left, player=player, message="")

        field = m.getField(player.coordX, player.coordY)

        if field == PRICKLY_VINE or field == LAVA:
            player.set_health(player.health - 5)
            m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20,
                             time=time_left, player=player, message="OUCH...")

        if (player.coordX, player.coordY) in m.items:
            item = m.items[(player.coordX, player.coordY)]
            message = ""
            if isinstance(item, Potion):
                if item.potion == PotionType.MEDICINE:
                    message = "You found some medicine. Press ENTER to put it in your backpack."
                if item.potion == PotionType.VODKA:
                    message = "You found some vodka. Press ENTER to put it in your backpack."
            if isinstance(item, Artifact):
                if item.artifact == ArtifactType.CLOWN_COSTUME:
                    message = "You found clown costume. Press ENTER to put it in your backpack."
            if isinstance(item, Treasure):
                message = "You found treasure. Press ENTER to collect it."
            m.drawPieceOfMap(centre_x=player.coordX, centre_y=player.coordY, height=20, width=20,
                             time=time_left, player=player, message=message)

    if DEAD:
        print("- - - \nOh, no... You are dead...\n- - - \nGAME OVER\n- - -")

    if TIMEOVER:
        print(
            "- - - \nTIME IS UP! You didn't escape the tombs so you became Tutankhamun's eternal slave.\n- - - \nGAME OVER\n- - -")

    if SUCCESS:
        print("- - - \n MISSION COMPLETED! You've collected all treasures! See you in the next tomb ;)\n- - -")


if __name__ == "__main__":
    main()
