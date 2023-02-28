import ply.yacc as yacc #Брала отсюда: https://github.com/dabeaz/ply
from interpreter_utils import AbstractCommand
from token_utils import tokens

class Parser:
    def __init__(self):
        def p_command(p):
            '''Command : Single_command_args
                        | Single_command
                        | Command_pipeline
                        | Environment_init Command
                        | Environment Command'''
        
        def p_command_pipeline(p):
            '''Command_pipeline : Single_command_args PIPELINE Command_pipeline
                                | Single_command PIPELINE Command_pipeline
                                | Single_command'''
        
        def p_single_command_args(p):
            'Single_command_args : NAME_COMMAND Args'
            if not p[1] in self.parser.commands:
                raise Exception("InvalidCommand") # TODO сори, я на винде, у меня не получилось termcolor установить
            if len(self.parser.args) != self.parser.commands[p[1]].number_of_inputs:
                raise Exception("InvalidNumberOfArguments") # TODO сори, я на винде, у меня не получилось termcolor установить
            self.parser.res += [AbstractCommand(p[1], self.parser.args)] # TODO надо там конструктор реализовать

        def p_single_command(p):
            'Single_command : NAME_COMMAND'
            if not p[1] in self.parser.commands:
                raise Exception("InvalidCommand") # TODO сори, я на винде, у меня не получилось termcolor установить
            k = 0
            if len(self.parser.res) > 0:
                k = self.parser.res[-1].number_of_outputs
            if k != self.parser.commands[p[1]].number_of_inputs:
                raise Exception("InvalidNumberOfArguments") # TODO сори, я на винде, у меня не получилось termcolor установить
            self.parser.res += [AbstractCommand(p[1], [])] # TODO надо там конструктор реализовать

        def p_environment_init(p):
            'Environment_init : VAR EQUALITY VALUE'
            self.parser.environment_variables[p[1]] = p[3]

        def p_args(p):
            '''Args : Arg
                    | Environment
                    | Arg Args
                    | Environment Args'''

        def p_arg(p):
            'Arg : ARG'
            self.parser.args += [p[1]]

        def p_environment(p):
            'Environment : DOLLAR VAR'
            self.parser.args += [self.parser.environment_variables[p[2]]]

        self.parser = yacc.yacc()
        self.parser.commands = []
        self.parser.environment_variables = []
        self.parser.args = []
        self.parser.res = []


    def parse(self, input, commands, environment_variables):
        self.parser.commands = commands
        self.parser.environment_variables = environment_variables
        self.parser.parse(input)
        return (self.parser.res, self.parser.environment_variables)