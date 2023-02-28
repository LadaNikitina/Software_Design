from termcolor import colored


class InterpreterException(Exception):
    message = colored("ERROR: an error occured while parsing or executing commands", 'red')


class InvalidNumberOfArguments(InterpreterException):
    message = colored("ERROR: found invalid number of arguments", 'red')


class InvalidCommand(InterpreterException):
    message = colored("ERROR: found invalid command", 'red')


class UnexpectedSymbol(InterpreterException):
    message = colored("ERROR: found unexpected symbol", 'red')
