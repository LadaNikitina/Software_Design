import re
from token_utils import Token_types, Token
# политика кавычек
# пайпы внутри кавычек есть текст
# $ внутри двойных кавычек есть переменная
# $ внутри одинарных кавычек есть текст

class Lexer():
    def lexer(self, string: str):
        token_specification = [
            ('var_var_quotes',               r'([A-Za-z][\_A-Za-z0-9]+)="\$([A-Za-z][\_A-Za-z0-9]+)"'), 
            ('var_var_no_quotes',            r'([A-Za-z][\_A-Za-z0-9]+)=\$([A-Za-z][\_A-Za-z0-9]+)'), 
            ('var_value_no_quotes',          r'([A-Za-z][\_A-Za-z0-9]+)=([^\s"\']+)'),
            ('var_value_single_quotes',      r'([A-Za-z][\_A-Za-z0-9]+)=\'([^\']*)\''),
            ('var_value_double_quotes',      r'([A-Za-z][\_A-Za-z0-9]+)="([^"]*)"'),
            ('pipeline_command',             r'\|\s*([A-Za-z][\_A-Za-z]+)'),
            ('pipeline_wrong',               r'\|\s*([^A-Za-z])'),
            ('command',                      r'^([A-Za-z][\_A-Za-z]+)'),
            ('arg_var_no_quotes',            r'\$([A-Za-z][\_A-Za-z0-9]+)'),
            ('arg_var_quotes',               r'"\$([A-Za-z][\_A-Za-z0-9]+)"'),
            ('arg_no_quotes',                r'([^\s"\'\|]+)'),
            ('arg_single_quotes',            r'\'([^\']*)\''),
            ('arg_double_quotes',            r'"([^"]*)"'),
            ('mismatch',                     r'.'),
        ]
            
        token_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
        all_tokens = []
        
        for mo in re.finditer(token_regex, string):
            kind = mo.lastgroup
            value = mo.group()
            if kind == 'var_var_quotes':
                var1, var2 = value.split("=")
                all_tokens.append(Token(Token_types.var, var1))
                all_tokens.append(Token(Token_types.assignment, "="))
                all_tokens.append(Token(Token_types.var, var2[2:-1]))
                break
            elif kind == 'var_var_no_quotes':
                var1, var2 = value.split("=")
                all_tokens.append(Token(Token_types.var, var1))
                all_tokens.append(Token(Token_types.assignment, "="))
                all_tokens.append(Token(Token_types.var, var2[1:]))
                break
            elif kind == 'var_value_no_quotes':
                var1, value2 = value.split("=")
                all_tokens.append(Token(Token_types.var, var1))
                all_tokens.append(Token(Token_types.assignment, "="))
                all_tokens.append(Token(Token_types.value, value2))
                break
            elif kind == 'var_value_single_quotes' or \
                 kind == 'var_value_double_quotes':
                var1, value2 = value.split("=")
                all_tokens.append(Token(Token_types.var, var1))
                all_tokens.append(Token(Token_types.assignment, "="))
                all_tokens.append(Token(Token_types.value, value2[1:-1]))
                break
            elif kind == 'command':
                all_tokens.append(Token(Token_types.command, value))
            elif kind == 'pipeline_command':
                all_tokens.append(Token(Token_types.pipeline, "|"))
                all_tokens.append(Token(Token_types.command, value[1:].strip()))
            elif kind == 'pipeline_wrong':
                break
            elif kind == 'arg_var_no_quotes':
                all_tokens.append(Token(Token_types.var, value[1:]))
            elif kind == 'arg_var_quotes':
                all_tokens.append(Token(Token_types.var, value[2:-1]))
            elif kind == 'arg_no_quotes':
                all_tokens.append(Token(Token_types.arg, value))   
            elif kind == 'arg_single_quotes' or \
                 kind == 'arg_double_quotes':
                all_tokens.append(Token(Token_types.arg, value[1:-1]))            
#             print(kind, value)
        return all_tokens
