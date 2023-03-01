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


def test_1():
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
    assert compare(tokens, right_tokens)


def test_2():
    tokens = lexer_obj.lexer('echo 1')
    right_tokens = [Token(Token_types.command, 'echo'),
                    Token(Token_types.arg, '1')]
    assert compare(tokens, right_tokens)


def test_3():
    tokens = lexer_obj.lexer('echo')
    right_tokens = [Token(Token_types.command, 'echo')]
    assert compare(tokens, right_tokens)


def test_4():
    tokens = lexer_obj.lexer('echo $var')
    right_tokens = [Token(Token_types.command, 'echo'),
                    Token(Token_types.var, 'var')]
    assert compare(tokens, right_tokens)


def test_5():
    tokens = lexer_obj.lexer('echo "$var"')
    right_tokens = [Token(Token_types.command, 'echo'),
                    Token(Token_types.var, 'var')]
    assert compare(tokens, right_tokens)


def test_6():
    tokens = lexer_obj.lexer("echo '$var'")
    right_tokens = [Token(Token_types.command, 'echo'),
                    Token(Token_types.arg, '$var')]
    assert compare(tokens, right_tokens)


def test_7():
    tokens = lexer_obj.lexer("exit")
    right_tokens = [Token(Token_types.command, 'exit')]
    assert compare(tokens, right_tokens)


def test_8():
    tokens = lexer_obj.lexer('echo 23 434 "454" "$dff"')
    right_tokens = [Token(Token_types.command, 'echo'),
                    Token(Token_types.arg, '23'),
                    Token(Token_types.arg, '434'),
                    Token(Token_types.arg, '454'),
                    Token(Token_types.var, 'dff')]
    assert compare(tokens, right_tokens)


def test_9():
    tokens = lexer_obj.lexer('pwd')
    right_tokens = [Token(Token_types.command, 'pwd')]
    assert compare(tokens, right_tokens)


def test_10():
    tokens = lexer_obj.lexer('cat /home/sergiy/tmp/file1')
    right_tokens = [Token(Token_types.command, 'cat'),
                    Token(Token_types.arg, '/home/sergiy/tmp/file1')]
    assert compare(tokens, right_tokens)


def test_11():
    tokens = lexer_obj.lexer('cat C:\\Users\\daled\\Downloads\\file\\baseline')
    right_tokens = [Token(Token_types.command, 'cat'),
                    Token(Token_types.arg, 'C:\\Users\\daled\\Downloads\\file\\baseline')]
    assert compare(tokens, right_tokens), "Oh no! Test №11 failed!"


def test_12():
    tokens = lexer_obj.lexer('wc /home/sergiy/tmp/file1')
    right_tokens = [Token(Token_types.command, 'wc'),
                    Token(Token_types.arg, '/home/sergiy/tmp/file1')]
    assert compare(tokens, right_tokens)


def test_13():
    tokens = lexer_obj.lexer('wc C:\\Users\\daled\\Downloads\\file\\baseline')
    right_tokens = [Token(Token_types.command, 'wc'),
                    Token(Token_types.arg, 'C:\\Users\\daled\\Downloads\\file\\baseline')]
    assert compare(tokens, right_tokens)


def test_14():
    tokens = lexer_obj.lexer('var=3')
    right_tokens = [Token(Token_types.var, 'var'),
                    Token(Token_types.assignment, '='),
                    Token(Token_types.value, '3')]
    assert compare(tokens, right_tokens)


def test_15():
    tokens = lexer_obj.lexer('var="3"')
    right_tokens = [Token(Token_types.var, 'var'),
                    Token(Token_types.assignment, '='),
                    Token(Token_types.value, '3')]
    assert compare(tokens, right_tokens)


def test_16():
    tokens = lexer_obj.lexer("var='3'")
    right_tokens = [Token(Token_types.var, 'var'),
                    Token(Token_types.assignment, '='),
                    Token(Token_types.value, '3')]
    assert compare(tokens, right_tokens)


def test_17():
    tokens = lexer_obj.lexer("var=$var1")
    right_tokens = [Token(Token_types.var, 'var'),
                    Token(Token_types.assignment, '='),
                    Token(Token_types.var, 'var1')]
    assert compare(tokens, right_tokens)


def test_18():
    tokens = lexer_obj.lexer("var='$var1'")
    right_tokens = [Token(Token_types.var, 'var'),
                    Token(Token_types.assignment, '='),
                    Token(Token_types.value, '$var1')]
    assert compare(tokens, right_tokens)


def test_19():
    tokens = lexer_obj.lexer('var="$var1"')
    right_tokens = [Token(Token_types.var, 'var'),
                    Token(Token_types.assignment, '='),
                    Token(Token_types.var, 'var1')]
    assert compare(tokens, right_tokens)


def test_20():
    tokens = lexer_obj.lexer('ls -l | grep "\.txt$"')
    right_tokens = [Token(Token_types.command, 'ls'),
                    Token(Token_types.arg, '-l'),
                    Token(Token_types.pipeline, '|'),
                    Token(Token_types.command, 'grep'),
                    Token(Token_types.arg, '\.txt$')]
    assert compare(tokens, right_tokens)


def test_21():
    tokens = lexer_obj.lexer('echo 1 | 45 67')
    right_tokens = [Token(Token_types.command, 'echo'),
                    Token(Token_types.arg, '1')]
    assert compare(tokens, right_tokens)


def test_22():
    tokens = lexer_obj.lexer('var=5 echo 1')
    right_tokens = [Token(Token_types.var, 'var'),
                    Token(Token_types.assignment, '='),
                    Token(Token_types.value, '5')]
    assert compare(tokens, right_tokens)
