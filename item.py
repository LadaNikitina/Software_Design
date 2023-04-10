class Item:
    def __init__(self, symbol, coordX, coordY):
        self.fieldSymbol = symbol
        self.coordX = coordX
        self.coordY = coordY


POISON = 'V'
ARTIFACT = '□'
TREASURE = '*'


class Poison(Item):
    def __init__(self, coordX, coordY):
        super().__init__(POISON, coordX, coordY)

        # Здесь должен быть случайный выбор одного из ядов
        self.stateItem = ''
        self.timeOfAction = 0

    def applyToCharacter(self):
        raise NotImplementedError()

    def isTimeUp(self):
        raise NotImplementedError()

    def removeFromCharacter(self):
        raise NotImplementedError()


class Artifact(Item):
    def __init__(self, coordX, coordY):
        super().__init__(ARTIFACT, coordX, coordY)

        # Здесь должен быть случайный выбор одного из артифактов
        self.stateItem = ''
        self.timeOfAction = 0
        self.ifRemovable = False

    def applyToCharacter(self):
        raise NotImplementedError()

    def isTimeUp(self):
        raise NotImplementedError()

    def removeFromCharacter(self):
        raise NotImplementedError()


class Treasure(Item):
    def __init__(self, coordX, coordY):
        super().__init__(TREASURE, coordX, coordY)

        # Здесь должен быть случайный выбор одного из сокровищ
        # TODO А разве cost не 1 всегда?
        self.cost = 0
