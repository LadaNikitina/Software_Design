class Character:
    def __init__(self, coordX, coordY):
        self.symbol = 'I'
        self.coordX = coordX
        self.coordY = coordY
        self.health = 300
        self.items = [] # сюда пихать айтемы
        self.power = 10
        self.treasures = 0 # для победы нужно собрать сокровища
        self.artifact = None # хранит используемые персонажем артефакты. нужен, чтобы уметь возвращать артефакты в инвентарь

    def move_up(self):
        self.coordX -= 1

    def move_down(self):
        self.coordX += 1

    def move_left(self):
        self.coordY -= 1

    def move_right(self):
        self.coordY += 1

    def set_health(self, new_health):
        self.health = max(new_health, 0)

    def set_power(self, new_power):
        self.power = max(new_power, 0)

    def add_item(self, item):
        self.items.append(item)

    def change_skin(self, new_skin):
        self.symbol = new_skin

    def set_standart_skin(self):
        self.symbol = 'I'

    def add_treasure(self, cost):
        self.treasures += cost