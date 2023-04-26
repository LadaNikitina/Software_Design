class Enemy:
    def __init__(self, symbol, coordX, coordY, experience, default_strategy, health, damage):
        self.symbol = symbol
        self.coordX = coordX
        self.coordY = coordY
        self.experience = experience
        self.default_strategy = default_strategy
        self.curr_strategy = default_strategy
        self.health = health
        self.damage = damage

    def change_health(self, d_health):
        self.health += d_health

        # Тут еще нужно что-то делать, если враг умер
        # А еще менять стратегию, если здоровья слишком мало или если оно нормализовалось (мб не порог устанавливать, а брать процент от максимального здоровья?)
        raise NotImplementedError()

# Функции ниже должны возвращать врага с нужными характеристиками
# К ним еще символы нужно придумать, берите те, что по ширине как буква латинская, а то бывают символы шире, из-за них карта поедет
def make_mummy(coordX, coordY):
    raise NotImplementedError()


def make_grasshopper(coordX, coordY):
    raise NotImplementedError()


def make_lost_traveler(coordX, coordY):
    raise NotImplementedError()
