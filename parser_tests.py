from parser_utils import Parser
from parser_utils import AbstractCommand # TODO
from lexer_utils import Lexer
import exceptions_utils

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

commands = ['echo', 'cat', 'wc', 'pwd', 'exit'] # там на деле dict должен быть

lexer = Lexer()
parser = Parser()

print("\nTEST1")
environment_variables = {}
tokens = lexer.lexer('nc -l 12345 | nc www.google.com 80 | nc www.google.com 80')
try:
    parser.parse(tokens, commands, environment_variables)
except exceptions_utils.InvalidCommand:
    print("Pass")

print("\nTEST2")
environment_variables = {}
right_res = [AbstractCommand('echo', ['1'])]
right_var = []
tokens = lexer.lexer('echo 1')
res, var = parser.parse(tokens, commands, environment_variables)
assert compare(right_res, right_var, res, var)
print("Pass")

print("\nTEST3")
environment_variables = {}
right_res = [AbstractCommand('echo', [])]
right_var = []
tokens = lexer.lexer('echo')
res, var = parser.parse(tokens, commands, environment_variables)
assert compare(right_res, right_var, res, var)
print("Pass")

print("\nTEST4")
environment_variables = {}
tokens = lexer.lexer('echo $var')
try:
    res, var = parser.parse(tokens, commands, environment_variables)
except exceptions_utils.UnknownVariable:
    print("Pass")

print("\nTEST5")
environment_variables = {}
right_res = [AbstractCommand('echo', ['$var'])]
right_var = []
tokens = lexer.lexer("echo '$var'")
res, var = parser.parse(tokens, commands, environment_variables)
assert compare(right_res, right_var, res, var)
print("Pass")

print("\nTEST6")
environment_variables = {}
right_res = [AbstractCommand('exit', [])]
right_var = []
tokens = lexer.lexer("exit")
res, var = parser.parse(tokens, commands, environment_variables)
assert compare(right_res, right_var, res, var)
print("Pass")

print("\nTEST7")
environment_variables = {}
tokens = lexer.lexer('echo 23 434 "454" "$dff"')
try:
    res, var = parser.parse(tokens, commands, environment_variables)
except exceptions_utils.UnknownVariable:
    print("Pass")

print("\nTEST8")
environment_variables = {}
right_res = [AbstractCommand('pwd', [])]
right_var = []
tokens = lexer.lexer('pwd')
res, var = parser.parse(tokens, commands, environment_variables)
assert compare(right_res, right_var, res, var)
print("Pass")

print("\nTEST9")
environment_variables = {}
right_res = [AbstractCommand('cat', ['/home/sergiy/tmp/file1'])]
right_var = []
tokens = lexer.lexer('cat /home/sergiy/tmp/file1')
res, var = parser.parse(tokens, commands, environment_variables)
assert compare(right_res, right_var, res, var)
print("Pass")

print("\nTEST10")
environment_variables = {}
right_res = [AbstractCommand('cat', ['C:\\Users\\daled\\Downloads\\file\\baseline'])]
right_var = []
tokens = lexer.lexer('cat C:\\Users\\daled\\Downloads\\file\\baseline')
res, var = parser.parse(tokens, commands, environment_variables)
assert compare(right_res, right_var, res, var)
print("Pass")

print("\nTEST11")
environment_variables = {}
right_res = [AbstractCommand('wc', ['/home/sergiy/tmp/file1'])]
right_var = []
tokens = lexer.lexer('wc /home/sergiy/tmp/file1')
res, var = parser.parse(tokens, commands, environment_variables)
assert compare(right_res, right_var, res, var)
print("Pass")

print("\nTEST12")
environment_variables = {}
right_res = [AbstractCommand('wc', ['C:\\Users\\daled\\Downloads\\file\\baseline'])]
right_var = []
tokens = lexer.lexer('wc C:\\Users\\daled\\Downloads\\file\\baseline')
res, var = parser.parse(tokens, commands, environment_variables)
assert compare(right_res, right_var, res, var)
print("Pass")

print("\nTEST13")
environment_variables = {}
right_res = []
right_var = {'var': '3'}
tokens = lexer.lexer('var=3')
res, var = parser.parse(tokens, commands, environment_variables)
assert compare(right_res, right_var, res, var)
print("Pass")

print("\nTEST14")
environment_variables = {}
tokens = lexer.lexer("var=$var1")
try:
    res, var = parser.parse(tokens, commands, environment_variables)
except exceptions_utils.UnknownVariable:
    print("Pass")

print("\nTEST15")
environment_variables = {}
right_res = []
right_var = {'var': '$var1'}
tokens = lexer.lexer("var='$var1'")
res, var = parser.parse(tokens, commands, environment_variables)
assert compare(right_res, right_var, res, var)
print("Pass")

print("\nTEST16")
environment_variables = {}
tokens = lexer.lexer('var="$var1"')
try:
    res, var = parser.parse(tokens, commands, environment_variables)
except exceptions_utils.UnknownVariable:
    print("Pass")

print("\nTEST17")
environment_variables = {}
tokens = lexer.lexer('ls -l | grep "\.txt$"')
try:
    parser.parse(tokens, commands, environment_variables)
except exceptions_utils.InvalidCommand:
    print("Pass")

print("\nTEST18")
environment_variables = {}
right_res = [AbstractCommand('echo', ['1'])]
right_var = {}
tokens = lexer.lexer('echo 1 | 45 67')
res, var = parser.parse(tokens, commands, environment_variables)
assert compare(right_res, right_var, res, var)
print("Pass")

print("\nTEST19")
environment_variables = {}
right_res = []
right_var = {'var': '5'}
tokens = lexer.lexer('var=5 echo 1')
res, var = parser.parse(tokens, commands, environment_variables)
assert compare(right_res, right_var, res, var)
print("Pass")
    
print("\nTEST20")
environment_variables = {}
right_res = [AbstractCommand('echo', ['1'])]
right_var = {'var': '1'}
tokens = lexer.lexer('var=1')
res, var = parser.parse(tokens, commands, environment_variables)
tokens = lexer.lexer('echo $var')
res, var = parser.parse(tokens, commands, var)
assert compare(right_res, right_var, res, var)
print("Pass")

print("\nTEST21")
environment_variables = {}
right_res = [AbstractCommand('echo', ['123']), AbstractCommand('wc', [])]
right_var = {}
tokens = lexer.lexer('echo 123 | wc')
res, var = parser.parse(tokens, commands, environment_variables)
assert compare(right_res, right_var, res, var)
print("Pass")

print("\nTEST22")
environment_variables = {}
right_res = [AbstractCommand('echo', ['1', '1', '1', '1', '1'])]
right_var = {}
tokens = lexer.lexer('echo 1 1 1 1 1')
res, var = parser.parse(tokens, commands, environment_variables)
assert compare(right_res, right_var, res, var)
print("Pass")

print("\nTEST23")
environment_variables = {}
right_res = [AbstractCommand('echo', ['2', '1', '1', '1', '1', '2'])]
right_var = {'var': '2'}
tokens = lexer.lexer('var=2')
res, var = parser.parse(tokens, commands, environment_variables)
tokens = lexer.lexer('echo $var 1 1 1 1 $var')
res, var = parser.parse(tokens, commands, var)
assert compare(right_res, right_var, res, var)
print("Pass")