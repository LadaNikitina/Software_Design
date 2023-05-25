import random
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

    def defensive_strategy(self, player_x, player_y, map):
        # В стратегии "defensive" монстр будет пытаться уйти от игрока
        # Он будет двигаться в противоположном направлении от игрока, если это безопасно
        new_x = self.coordX
        new_y = self.coordY
        dx = self.coordX - player_x
        dy = self.coordY - player_y

        # Определяем направление, в котором нужно двигаться в противоположном направлении от игрока
        if random.randint(0, 100) >= 50:
            if dx > 0:
                new_x = self.coordX + 1
            elif dx < 0:
                new_x = self.coordX - 1
        else:
            if dy > 0:
                new_y = self.coordY + 1
            elif dy < 0:
                new_y = self.coordY - 1

        # Проверяем, является ли новая позиция безопасной на карте
        if map.is_valid_position(new_x, new_y):
            self.coordX = new_x
            self.coordY = new_y

    def aggressive_strategy(self, player_x, player_y, map):
        # В стратегии "aggressive" монстр будет преследовать игрока и атаковать его
        new_x = self.coordX
        new_y = self.coordY
        dx = self.coordX - player_x
        dy = self.coordY - player_y

        # Проверяем, является ли игрок достаточно близким для атаки
        if abs(dx) <= 1 and abs(dy) <= 1:
            self.attack_player(player_x, player_y)
        else:
            if random.randint(0, 100) >= 50:
                if dx > 0:
                    new_x = self.coordX - 1
                elif dx < 0:
                    new_x = self.coordX + 1
            else:
                if dy > 0:
                    new_y = self.coordY - 1
                elif dy < 0:
                    new_y = self.coordY + 1


    def passive_strategy(self, player_x, player_y, map):

        # В стратегии "passive" монстр будет игнорировать игрока и двигаться случайно по карте

        # Реализуйте здесь логику для случайного движения монстра

    def move_away_from_player(self, player_x, player_y, map):

        # Реализуйте здесь логику движения монстра в противоположном направлении от игрока

    def attack_player(self, player_x, player_y):

        # Реализуйте здесь атаку монстра на игрока

    def ignore_player(self):
        # Реализуйте здесь игнорирование игрока


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

