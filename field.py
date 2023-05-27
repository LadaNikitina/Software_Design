class Field:
    def __init__(self, symbol):
        self.fieldSymbol = symbol


NOTHING = Field(' ')
WALL = Field('█')


class Trap(Field):
    def __init__(self, symbol):
        super().__init__(symbol)

    def applyDamage(self, player):
        player.set_health(player.health - 5)


PRICKLY_VINE = Trap('░')
LAVA = Trap('▓')
