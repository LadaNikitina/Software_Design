from parser_utils import Parser
from command_utils import AbstractCommand
from lexer_utils import Lexer
import exceptions_utils
import pytest

def compare(res1, var1, res2, var2):
    if len(res1) != len(res2) or len(var1) != len(var2):
        return False
    for i in range(len(res1)):
        if res1[i].name != res2[i].name:
            return False
        if len(res1[i].args) != len(res2[i].args):
            return False
        for j in range(len(res1[i].args)):
            if res1[i].args[j] != res2[i].args[j]:
                return False
    for i in var1:
        if not i in var2:
            return False
        if var1[i] != var2[i]:
            return False
    return True

lexer = Lexer()
parser = Parser()

def test_1():
    environment_variables = {}
    right_res = [AbstractCommand('echo', ['2', '1', '1', '1', '1', '2'])]
    right_var = {'var': '2'}
    tokens = lexer.lexer('var=2')
    res, var = parser.parse(tokens, environment_variables)
    tokens = lexer.lexer('echo $var 1 1 1 1 $var')
    res, var = parser.parse(tokens, var)
    assert compare(right_res, right_var, res, var)

def test_2():
    environment_variables = {}
    right_res = [AbstractCommand('echo', ['1'])]
    right_var = []
    tokens = lexer.lexer('echo 1')
    res, var = parser.parse(tokens, environment_variables)
    assert compare(right_res, right_var, res, var)

def test_3():
    environment_variables = {}
    right_res = [AbstractCommand('echo', [])]
    right_var = []
    tokens = lexer.lexer('echo')
    res, var = parser.parse(tokens, environment_variables)
    assert compare(right_res, right_var, res, var)

def test_4():
    with pytest.raises(exceptions_utils.UnknownVariable):
        environment_variables = {}
        tokens = lexer.lexer('echo $var')
        res, var = parser.parse(tokens, environment_variables)

def test_5():
    environment_variables = {}
    right_res = [AbstractCommand('echo', ['$var'])]
    right_var = []
    tokens = lexer.lexer("echo '$var'")
    res, var = parser.parse(tokens, environment_variables)
    assert compare(right_res, right_var, res, var)


def test_6():
    environment_variables = {}
    right_res = [AbstractCommand('exit', [])]
    right_var = []
    tokens = lexer.lexer("exit")
    res, var = parser.parse(tokens, environment_variables)
    assert compare(right_res, right_var, res, var)

def test_7():
    with pytest.raises(exceptions_utils.UnknownVariable):
        environment_variables = {}
        tokens = lexer.lexer('echo 23 434 "454" "$dff"')
        res, var = parser.parse(tokens, environment_variables)


def test_8():
    environment_variables = {}
    right_res = [AbstractCommand('pwd', [])]
    right_var = []
    tokens = lexer.lexer('pwd')
    res, var = parser.parse(tokens, environment_variables)
    assert compare(right_res, right_var, res, var)


def test_9():
    environment_variables = {}
    right_res = [AbstractCommand('cat', ['/home/sergiy/tmp/file1'])]
    right_var = []
    tokens = lexer.lexer('cat /home/sergiy/tmp/file1')
    res, var = parser.parse(tokens, environment_variables)
    assert compare(right_res, right_var, res, var)


def test_10():
    environment_variables = {}
    right_res = [AbstractCommand('cat', ['C:\\Users\\daled\\Downloads\\file\\baseline'])]
    right_var = []
    tokens = lexer.lexer('cat C:\\Users\\daled\\Downloads\\file\\baseline')
    res, var = parser.parse(tokens, environment_variables)
    assert compare(right_res, right_var, res, var)


def test_11():
    environment_variables = {}
    right_res = [AbstractCommand('wc', ['/home/sergiy/tmp/file1'])]
    right_var = []
    tokens = lexer.lexer('wc /home/sergiy/tmp/file1')
    res, var = parser.parse(tokens, environment_variables)
    assert compare(right_res, right_var, res, var)


def test_12():
    environment_variables = {}
    right_res = [AbstractCommand('wc', ['C:\\Users\\daled\\Downloads\\file\\baseline'])]
    right_var = []
    tokens = lexer.lexer('wc C:\\Users\\daled\\Downloads\\file\\baseline')
    res, var = parser.parse(tokens, environment_variables)
    assert compare(right_res, right_var, res, var)


def test_13():
    environment_variables = {}
    right_res = []
    right_var = {'var': '3'}
    tokens = lexer.lexer('var=3')
    res, var = parser.parse(tokens, environment_variables)
    assert compare(right_res, right_var, res, var)

def test_14():
    with pytest.raises(exceptions_utils.UnknownVariable):
        environment_variables = {}
        tokens = lexer.lexer("var=$var1")
        res, var = parser.parse(tokens, environment_variables)


def test_15():
    environment_variables = {}
    right_res = []
    right_var = {'var': '$var1'}
    tokens = lexer.lexer("var='$var1'")
    res, var = parser.parse(tokens, environment_variables)
    assert compare(right_res, right_var, res, var)


def test_16():
    with pytest.raises(exceptions_utils.UnknownVariable):
        environment_variables = {}
        tokens = lexer.lexer('var="$var1"')
        res, var = parser.parse(tokens, environment_variables)

def test_17():
    environment_variables = {}
    right_res = [AbstractCommand('ls', ['-l']), AbstractCommand('grep', ['\.txt$'])]
    right_var = {}
    tokens = lexer.lexer('ls -l | grep "\.txt$"')
    res, var = parser.parse(tokens, environment_variables)
    assert compare(right_res, right_var, res, var)


def test_18():
    environment_variables = {}
    right_res = [AbstractCommand('echo', ['1'])]
    right_var = {}
    tokens = lexer.lexer('echo 1 | 45 67')
    res, var = parser.parse(tokens, environment_variables)
    assert compare(right_res, right_var, res, var)


def test_19():
    environment_variables = {}
    right_res = []
    right_var = {'var': '5'}
    tokens = lexer.lexer('var=5 echo 1')
    res, var = parser.parse(tokens, environment_variables)
    assert compare(right_res, right_var, res, var)

    
def test_20():
    environment_variables = {}
    right_res = [AbstractCommand('echo', ['1'])]
    right_var = {'var': '1'}
    tokens = lexer.lexer('var=1')
    res, var = parser.parse(tokens, environment_variables)
    tokens = lexer.lexer('echo $var')
    res, var = parser.parse(tokens, var)
    assert compare(right_res, right_var, res, var)


def test_21():
    environment_variables = {}
    right_res = [AbstractCommand('echo', ['123']), AbstractCommand('wc', [])]
    right_var = {}
    tokens = lexer.lexer('echo 123 | wc')
    res, var = parser.parse(tokens, environment_variables)
    assert compare(right_res, right_var, res, var)


def test_22():
    environment_variables = {}
    right_res = [AbstractCommand('echo', ['1', '1', '1', '1', '1'])]
    right_var = {}
    tokens = lexer.lexer('echo 1 1 1 1 1')
    res, var = parser.parse(tokens, environment_variables)
    assert compare(right_res, right_var, res, var)
