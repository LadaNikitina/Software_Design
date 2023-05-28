import random
from enum import Enum


class Item:
    def __init__(self, symbol, coordX, coordY):
        self.fieldSymbol = symbol
        self.coordX = coordX
        self.coordY = coordY
        self.name = ""
        self.descr = ""

    def pickUpItem(self, character):
        character.add_item(self)

    def applyToCharacter(self, character):
        pass

    def returnToInventory(self, character):
        pass


POTION = '@'
ARTIFACT = '□'
TREASURE = '*'


class PotionType(Enum):
    MEDICINE = 1  # восстанавливает здоровье
    VODKA = 2  # увеличивает силу игрока


class Potion(Item):
    def __init__(self, coordX, coordY):
        super().__init__(POTION, coordX, coordY)
        self.potion = random.choice([PotionType.MEDICINE, PotionType.VODKA])
        self.fieldSymbol = POTION
        if self.potion == PotionType.MEDICINE:
            self.name = "medicine"
            self.descr = "Increases health by 10 points."
        if self.potion == PotionType.VODKA:
            self.name = "vodka"
            self.descr = "Increases power by 10 points."

    def applyToCharacter(self, character):
        if self.potion == PotionType.MEDICINE:
            character.set_health(character.health + 10)
        if self.potion == PotionType.VODKA:
            character.set_power(character.power + 10)


class ArtifactType(Enum):
    CLOWN_COSTUME = 1  # не дает игроку никаких преимуществ, надевая его, игрок просто выглядит глупо.
    # меняет отображение символа I персонажа на Z


class Artifact(Item):
    def __init__(self, coordX, coordY):
        super().__init__(ARTIFACT, coordX, coordY)
        self.artifact = random.choice([ArtifactType.CLOWN_COSTUME])
        if ArtifactType.CLOWN_COSTUME:
            self.name = "clown costume"
            self.descr = "Doesn't give you any advantages. You look like an idiot when you wear it."
            self.message = "You are wearing a clown costume."

    def applyToCharacter(self, character):
        if self.artifact == ArtifactType.CLOWN_COSTUME:
            character.change_skin('Z')

    def returnToInventory(self, character):
        if self.artifact == ArtifactType.CLOWN_COSTUME:
            character.set_standart_skin()
        character.add_item(self)


class Treasure(Item):
    def __init__(self, coordX, coordY):
        super().__init__(TREASURE, coordX, coordY)
        self.cost = 1

    def applyToCharacter(self, character):
        character.add_treasure(self.cost)
