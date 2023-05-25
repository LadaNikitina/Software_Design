class Character:
    def __init__(self, coordX, coordY):
        self.coordX = coordX
        self.coordY = coordY
        self.health = 100
        self.items = [] # сюда пихать айтемы
        self.experience = 0

    def move_up(self):
        self.coordX -= 1

    def move_down(self):
        self.coordX += 1

    def move_left(self):
        self.coordY -= 1

    def move_right(self):
        self.coordY += 1
