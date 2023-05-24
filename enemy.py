class Enemy:
    def __init__(self, symbol, coordX, coordY, experience, default_strategy, health, damage):
        self.symbol = symbol
        self.coordX = coordX
        self.coordY = coordY
        self.experience = experience
        self.default_strategy = default_strategy
        self.curr_strategy = default_strategy
        self.health = health
        self.max_health = health
        self.damage = damage
        self.is_alive = True

    def change_health(self):
        if self.health <= 0:
            self.is_alive = False
            # тут по флагу с карты эта дичь удаляется
        elif self.health < 0.2 * self.max_health:
            self.curr_strategy = "defensive"
        elif self.health >= 0.8 * self.max_health:
            self.curr_strategy = self.default_strategy

    def outer_damage(self, damage):
        self.health = min(0, self.health - damage)
        self.change_health()

    def hill(self, hill_value):
        self.health = max(self.max_health, self.health + hill_value)
        self.change_health()


# Функции ниже должны возвращать врага с нужными характеристиками
# К ним еще символы нужно придумать, берите те, что по ширине как буква латинская, а то бывают символы шире, из-за них карта поедет
def make_mummy(coordX, coordY):
    symbol = "M"
    experience = 50
    default_strategy = "aggressive"
    health = 100
    damage = 10

    enemy = Enemy(symbol, coordX, coordY, experience, default_strategy, health, damage)
    return enemy


def make_grasshopper(coordX, coordY):
    symbol = "G"
    experience = 30
    default_strategy = "defensive"
    health = 50
    damage = 5
    enemy = Enemy(symbol, coordX, coordY, experience, default_strategy, health, damage)
    return enemy


def make_lost_traveler(coordX, coordY):
    symbol = "T"
    experience = 20
    default_strategy = "passive"
    health = 30
    damage = 2
    enemy = Enemy(symbol, coordX, coordY, experience, default_strategy, health, damage)
    return enemy
