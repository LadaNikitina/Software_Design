from sys import stdin,  exit
from lexer_utils import Lexer
from token_utils import Token
from exceptions_utils import InterpreterException

class Parser:
    def parse(self):
        commands = []
        commands.append(EchoCommand())
        commands.append(ExitCommand())
        return commands

class Interpreter():
    lexer = Lexer()
    parser = Parser()
    environment_variables = dict()

    def run(self):
        for line in stdin:
            try:
                #lexer
                #where we substitute env vars with their values??
                commands = self.parser.parse()
                prev_result = "" #we need it for pipes
                for command in commands:
                    command.args += f" {prev_result}"
                    prev_result = command.execute()
            except InterpreterException as error:
                print(error)




class AbstractCommand:
    name = "command"
    def execute(self):
        print("successfully executed command")
        return "result"

class EchoCommand(AbstractCommand):
    name = "echo"
    args = "some text"
    def execute(self):
        print("echo command successfully executed")
        return self.args

class ExitCommand(AbstractCommand):
    name = "exit"
    args = ""
    def execute(self):
        print("exiting interpreter")
        exit()
