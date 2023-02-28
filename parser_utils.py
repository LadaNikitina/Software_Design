#from interpreter_utils import AbstractCommand TODO
import exceptions_utils
from token_utils import Token_types

# TODO надо удалить, когда реализован будет
class AbstractCommand():
    def __init__(self, name, args):
        self.name = name
        self.args = args
    
class Parser():
    def __init__(self):
        self.commands = []
        self.environment_variables = []
        self.res = []

    def p_command(self, input):
        '''Command : Environments_init
                    | Command_pipeline
                    | Single_command'''
        if len(input) == 0:
            return True
        if self.p_environments_init(input):
            return True
        if self.p_command_pipeline(input):
            return True
        if self.p_single_command(input):
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
        '''Environment_init : VAR ASSIGNMENT VALUE
                            | VAR ASSIGNMENT VAR'''
        if len(input) != 3:
            return False
        if input[0].token_type == Token_types.var and input[1].token_type == Token_types.assignment and input[2].token_type == Token_types.value:
            self.environment_variables[input[0].token_value] = input[2].token_value
            return True
        if input[0].token_type == Token_types.var and input[1].token_type == Token_types.assignment and input[2].token_type == Token_types.var:
            if not input[2].token_value in self.environment_variables:
                raise exceptions_utils.UnknownVariable()
            self.environment_variables[input[0].token_value] = self.environment_variables[input[2].token_value]
            return True
        return False

    def p_command_pipeline(self, input):
        '''Command_pipeline : Single_command PIPELINE Command_pipeline
                            | Single_command'''
        if len(input) == 0:
            return True
        for i in range(len(input)):
            if input[i].token_type == Token_types.pipeline:
                if self.p_single_command(input[:i]) and self.p_command_pipeline(input[i+1:]):
                    return True
                else:
                    return False
        if self.p_single_command(input):
            return True
        return False
        
    def p_single_command(self, input):
        'Single_command : COMMAND Args'
        if len(input) == 0 or input[0].token_type != Token_types.command:
            return False
        
        if not input[0].token_value in self.commands:
            raise exceptions_utils.InvalidCommand()
        
        (fl, args) = self.p_args(input[1:])
        if not fl:
            return False
        
        self.res += [AbstractCommand(input[0].token_value, args)]
        return True

    def p_args(self, input):
        '''Args : ARG
                | ARG Args
                | Environment Args
                | Environment'''
        if len(input) == 0:
            return (True, [])

        if len(input) == 1 and input[0].token_type == Token_types.arg:
            return (True, [input[0].token_value])

        if input[0].token_type == Token_types.arg:
            (fl, args) = self.p_args(input[1:])
            if fl:
                return (True, [input[0].token_value] + args)
            return (False, [])

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
        
        (fl, arg) = self.p_environment(input)
        if fl:
            return (True, [arg])
        
        return (False, [])
                
    def p_environment(self, input):
        'Environment : VAR'
        if len(input) != 1 or input[0].token_type != Token_types.var:
            return (False, None)
        if not input[0].token_value in self.environment_variables:
            raise exceptions_utils.UnknownVariable()
        return (True, self.environment_variables[input[0].token_value])

    def parse_tokens(self, input):
        if not self.p_command(input):
            raise exceptions_utils.ParsingError()

    def parse(self, input, commands, environment_variables):
        self.commands = commands
        self.environment_variables = environment_variables
        self.res = []
        self.parse_tokens(input)
        return (self.res, self.environment_variables)