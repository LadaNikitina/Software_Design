class Field:
    def __init__(self, symbol):
        self.fieldSymbol = symbol


NOTHING = Field(' ')
WALL = Field('█')


class Trap(Field):
    def __init__(self, symbol):
        super().__init__(symbol)

    def applyDamage(self):
        raise NotImplementedError()


PRICKLY_VINE = Trap('░')
LAVA = Trap('▓')
