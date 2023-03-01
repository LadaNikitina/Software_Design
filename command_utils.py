from abc import abstractmethod
from os import popen
from exceptions_utils import EmptyFilename, InvalidCommand


class AbstractCommand:

    def __init__(self, name="", args=""):
        self.name = name
        self.args = args

    @abstractmethod
    def execute(self, show_output=True):
        pass


class CatCommand(AbstractCommand):

    def __init__(self, args):
        super().__init__(name="cat", args=args)
        if self.args == "":
            raise EmptyFilename

    def execute(self, show_output=True):
        filename = ""
        for arg in self.args:
            filename += " "
            filename += arg
        output = popen(f"cat{filename}").read()
        if show_output:
            print(output, end="")
        return output


class EchoCommand(AbstractCommand):

    def __init__(self, args=""):
        super().__init__(name="echo", args=args)

    def execute(self, show_output=True):
        output = ""
        for arg in self.args:
            output += arg
            output += " "
        if show_output:
            print(output)
        return output


class PwdCommand(AbstractCommand):

    def __init__(self):
        super().__init__(name="pwd")

    def execute(self, show_output=True):
        output = popen("pwd").read()
        if show_output:
            print(output, end="")
        return output


class WcCommand(AbstractCommand):

    def __init__(self, args):
        super().__init__(name="wc", args=args)
        if self.args == "":
            raise EmptyFilename

    def execute(self, show_output=True):
        filename = ""
        for arg in self.args:
            filename += " "
            filename += arg
        output = popen(f"wc{filename}").read()
        if show_output:
            print(output, end="")
        return output


class ExitCommand(AbstractCommand):

    def __init__(self):
        super().__init__(name="exit")

    def execute(self, show_output=False):
        exit()


class OtherCommand(AbstractCommand):

    def __init__(self, name, args):
        super().__init__(name, args)
        if name == "" and args != "":
            raise InvalidCommand

    def execute(self, show_output=True):
        args = ""
        output = popen(f"{self.name} {self.args}").read()
        if show_output:
            print(output, end="")
        return output
