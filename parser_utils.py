from interpreter_utils import AbstractCommand
from token_utils import Token_types

class Parser:
    def __init__(self):
        self.commands = []
        self.environment_variables = []
        self.res = []

    def p_command(self, input):
        '''Command : Single_command
                    | Environments_init
                    | Command_pipeline'''
        if len(input) == 0:
            return True
        if self.p_single_command(input):
            return True
        if self.p_environments_init(input):
            return True
        if self.p_command_pipeline(input):
            return True
        return False
    
    def p_environments_init(self, input):
        '''Environments_init : Environment_init
                            |  Environment_init Environments_init'''
        if len(input) == 0:
            return True
        if self.p_environment_init(input):
            return True
        
        for i in range(len(input)):
            if input[i].token_type == Token_types.value:
                if self.p_environment_init(input[:i+1]) and self.p_environments_init(input[i+1:]):
                    return True
                else:
                    return False
        return False

    def p_environment_init(self, input):
        'Environment_init : VAR EQUALITY VALUE'
        if len(input) != 3:
            return False
        if input[0].token_type == Token_types.var and input[1].token_type == Token_types.equality and input[2].token_type == Token_types.value:
            self.environment_variables[input[0].token_value] = [input[2].token_value]
            return True
        return False

    def p_command_pipeline(self, input):
        '''Command_pipeline : Single_command
                            | Single_command PIPELINE Command_pipeline'''
        if len(input) == 0:
            return True
        if self.p_single_command(input):
            return True
        for i in range(len(input)):
            if input[i].token_type == Token_types.pipeline:
                if self.p_single_command(input[:i]) and self.p_command_pipeline(input[i+1:]):
                    return True
                else:
                    return False
        return False
        
    def p_single_command(self, input):
        'Single_command : NAME_COMMAND Args'
        if len(input) == 0 or input[0].token_type != Token_types.command:
            return False
        
        if not input[0] in self.parser.commands:
            raise Exception("Invalid command")
        
        (fl, args) = self.p_args(input[1:])
        if not fl:
            return False
        
        self.res += [AbstractCommand(input[0].token_value, args)]
        return True

    def p_args(self, input):
        '''Args : ARG
                | ARG Args
                | Environment
                | Environment Args'''
        if len(input) == 0:
            return (True, [])

        if len(input) == 1 and input[0].token_type == Token_types.arg:
            return (True, [input[0].token_value])

        if input[0].token_type == Token_types.arg:
            (fl, args) = self.p_args(input[1:])
            if fl:
                return (True, [input[0].token_value] + args)
            return (False, [])

        (fl, arg) = self.p_environment(input)
        if fl:
            return (True, [arg])

        for i in range(len(input)):
            if input[i].token_type == Token_types.var:
                (fl, arg) = self.p_environment(input[:i+1])
                if not fl:
                    return (False, [])
                (fl, args) = self.p_args(input[i+1:])
                if fl:
                    return (True, [arg] + args)
                else:
                    return (False, [])
                
    def p_environment(self, input):
        'Environment : DOLLAR VAR'
        if len(input) != 2 or input[0].token_type != Token_types.dollar or input[1].token_type != Token_types.var:
            return (False, None)
        if not input[1].token_value in self.environment_variables:
            raise Exception("Unknown environment variables")
        return (True, self.environment_variables[input[1].token_value])

    def parse_tokens(self, input):
        if not self.p_command(input):
            raise Exception("Parse error")

    def parse(self, input, commands, environment_variables):
        self.commands = commands
        self.environment_variables = environment_variables
        self.parse_tokens(input)
        return (self.res, self.environment_variables)