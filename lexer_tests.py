from token_utils import Token_types, Token
from lexer_utils import Lexer

def compare(tokens1, tokens2):
    if len(tokens1) != len(tokens2):
        return False
    for token1, token2 in zip(tokens1, tokens2):
        if not token1 == token2:
            return False
    return True
    

lexer_obj = Lexer()
tokens = lexer_obj.lexer('nc -l 12345 | nc www.google.com 80 | nc www.google.com 80')
right_tokens = [Token(Token_types.command, 'nc'),
                Token(Token_types.arg, '-l'),
                Token(Token_types.arg, '12345'),
                Token(Token_types.pipeline, '|'),
                Token(Token_types.command, 'nc'),
                Token(Token_types.arg, 'www.google.com'),
                Token(Token_types.arg, '80'),
                Token(Token_types.pipeline, '|'),
                Token(Token_types.command, 'nc'),
                Token(Token_types.arg, 'www.google.com'),
                Token(Token_types.arg, '80')]
assert compare(tokens, right_tokens), "Oh no! Test №1 failed!"


tokens = lexer_obj.lexer('echo 1')
right_tokens = [Token(Token_types.command, 'echo'),
                Token(Token_types.arg, '1')]
assert compare(tokens, right_tokens), "Oh no! Test №2 failed!"


tokens = lexer_obj.lexer('echo')
right_tokens = [Token(Token_types.command, 'echo')]
assert compare(tokens, right_tokens), "Oh no! Test №3 failed!"


tokens = lexer_obj.lexer('echo $var')
right_tokens = [Token(Token_types.command, 'echo'),
                Token(Token_types.var, 'var')]
assert compare(tokens, right_tokens), "Oh no! Test №4 failed!"


tokens = lexer_obj.lexer('echo "$var"')
right_tokens = [Token(Token_types.command, 'echo'),
                Token(Token_types.var, 'var')]
assert compare(tokens, right_tokens), "Oh no! Test №5 failed!"


tokens = lexer_obj.lexer("echo '$var'")
right_tokens = [Token(Token_types.command, 'echo'),
                Token(Token_types.arg, '$var')]
assert compare(tokens, right_tokens), "Oh no! Test №6 failed!"


tokens = lexer_obj.lexer("exit")
right_tokens = [Token(Token_types.command, 'exit')]
assert compare(tokens, right_tokens), "Oh no! Test №7 failed!"


tokens = lexer_obj.lexer('echo 23 434 "454" "$dff"')
right_tokens = [Token(Token_types.command, 'echo'),
                Token(Token_types.arg, '23'),
                Token(Token_types.arg, '434'),
                Token(Token_types.arg, '454'),
                Token(Token_types.var, 'dff')]
assert compare(tokens, right_tokens), "Oh no! Test №8 failed!"


tokens = lexer_obj.lexer('pwd')
right_tokens = [Token(Token_types.command, 'pwd')]
assert compare(tokens, right_tokens), "Oh no! Test №9 failed!"


tokens = lexer_obj.lexer('cat /home/sergiy/tmp/file1')
right_tokens = [Token(Token_types.command, 'cat'),
                Token(Token_types.arg, '/home/sergiy/tmp/file1')]
assert compare(tokens, right_tokens), "Oh no! Test №10 failed!"


tokens = lexer_obj.lexer('cat C:\\Users\\daled\\Downloads\\file\\baseline')
right_tokens = [Token(Token_types.command, 'cat'),
                Token(Token_types.arg, 'C:\\Users\\daled\\Downloads\\file\\baseline')]
assert compare(tokens, right_tokens), "Oh no! Test №11 failed!"


tokens = lexer_obj.lexer('wc /home/sergiy/tmp/file1')
right_tokens = [Token(Token_types.command, 'wc'),
                Token(Token_types.arg, '/home/sergiy/tmp/file1')]
assert compare(tokens, right_tokens), "Oh no! Test №10 failed!"


tokens = lexer_obj.lexer('wc C:\\Users\\daled\\Downloads\\file\\baseline')
right_tokens = [Token(Token_types.command, 'wc'),
                Token(Token_types.arg, 'C:\\Users\\daled\\Downloads\\file\\baseline')]
assert compare(tokens, right_tokens), "Oh no! Test №11 failed!"


tokens = lexer_obj.lexer('var=3')
right_tokens = [Token(Token_types.var, 'var'),
                Token(Token_types.assignment, '='),
                Token(Token_types.value, '3')]
assert compare(tokens, right_tokens), "Oh no! Test №12 failed!"


tokens = lexer_obj.lexer('var="3"')
right_tokens = [Token(Token_types.var, 'var'),
                Token(Token_types.assignment, '='),
                Token(Token_types.value, '3')]
assert compare(tokens, right_tokens), "Oh no! Test №13 failed!"


tokens = lexer_obj.lexer("var='3'")
right_tokens = [Token(Token_types.var, 'var'),
                Token(Token_types.assignment, '='),
                Token(Token_types.value, '3')]
assert compare(tokens, right_tokens), "Oh no! Test №14 failed!"


tokens = lexer_obj.lexer("var=$var1")
right_tokens = [Token(Token_types.var, 'var'),
                Token(Token_types.assignment, '='),
                Token(Token_types.var, 'var1')]
assert compare(tokens, right_tokens), "Oh no! Test №15 failed!"


tokens = lexer_obj.lexer("var='$var1'")
right_tokens = [Token(Token_types.var, 'var'),
                Token(Token_types.assignment, '='),
                Token(Token_types.value, '$var1')]
assert compare(tokens, right_tokens), "Oh no! Test №16 failed!"


tokens = lexer_obj.lexer('var="$var1"')
right_tokens = [Token(Token_types.var, 'var'),
                Token(Token_types.assignment, '='),
                Token(Token_types.var, 'var1')]
assert compare(tokens, right_tokens), "Oh no! Test №17 failed!"


tokens = lexer_obj.lexer('ls -l | grep "\.txt$"')
right_tokens = [Token(Token_types.command, 'ls'),
                Token(Token_types.arg, '-l'),
                Token(Token_types.pipeline, '|'),
                Token(Token_types.command, 'grep'),
                Token(Token_types.arg, '\.txt$')]
assert compare(tokens, right_tokens), "Oh no! Test №18 failed!"

tokens = lexer_obj.lexer('echo 1 | 45 67')
right_tokens = [Token(Token_types.command, 'echo'),
                Token(Token_types.arg, '1')]
assert compare(tokens, right_tokens), "Oh no! Test №19 failed!"

tokens = lexer_obj.lexer('var=5 echo 1')
right_tokens = [Token(Token_types.var, 'var'),
                Token(Token_types.assignment, '='),
                Token(Token_types.value, '5')]
assert compare(tokens, right_tokens), "Oh no! Test №20 failed!"