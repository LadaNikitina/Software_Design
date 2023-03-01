from sys import stdin
from lexer_utils import Lexer
from parser_utils import Parser
from exceptions_utils import InterpreterException
from command_utils import *


def create_command(abstract_command, prev_result):
    if prev_result != "":
        abstract_command.args.append(prev_result)
    match abstract_command.name:
        case "cat":
            command = CatCommand(abstract_command.args)
        case "echo":
            command = EchoCommand(abstract_command.args)
        case "pwd":
            command = PwdCommand()
        case "wc":
            command = WcCommand(abstract_command.args)
        case "exit":
            command = ExitCommand()
        case _:
            command = OtherCommand(abstract_command.name, abstract_command.args)
    return command


class Interpreter:
    def __init__(self):
        self.lexer = Lexer()
        self.parser = Parser()
        self.environment_variables = dict()

    def run(self):
        for line in stdin:
            try:
                tokens = self.lexer.lexer(line)
                abstract_commands, self.environment_variables = self.parser.parse(tokens, self.environment_variables)
                prev_result = ""
                for i in range(len(abstract_commands)):
                    a_c = abstract_commands[i]
                    command = create_command(a_c, prev_result)
                    show = (i == len(abstract_commands) - 1)
                    prev_result = command.execute(show)
            except InterpreterException as error:
                print(error)
