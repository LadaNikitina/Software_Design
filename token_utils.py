from enum import Enum

Token_types = Enum('Token_types', [
                             'command',       # команда
                             'arg',           # аргумент
                             'equality',      # знак равенства
                             'dollar',        # знак доллара
                             'var',           # переменная
                             'value',         # значение переменной
                             'double_quotes', # двойные кавычки
                             'pipeline',      # пайплайн
                             'single_quotes'  # одинарные кавычки
                        ]
             )

class Token():
    token_type: Token_types = None
    token_value: str = None
        
    def __init__(self, token_type, token_value):
        self.token_type = token_type
        self.token_value = token_value
        
# пример
# example_token = Token(Token_types.equality, '=')