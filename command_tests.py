from command_utils import EchoCommand, CatCommand, PwdCommand, WcCommand, ExitCommand
from os import getcwd


def test_echo_simple():
    # echo "Hello, World"
    args = ["Hello, World"]
    command = EchoCommand(args)
    result = command.execute()
    assert args[0] == result.rstrip()


def test_echo_multiple_args():
    # echo 1      2
    args = ['1', '2']
    command = EchoCommand(args)
    result = command.execute()
    assert args[0] + ' ' + args[1] == result.rstrip()


def test_cat_simple():
    # cat test_files/a.txt
    args = ['test_files/a.txt']
    command = CatCommand(args)
    result = command.execute()
    assert "1" == result.rstrip()


def test_cat_multiple_args():
    # cat test_files/a.txt  test_files/b.txt
    args = ['test_files/a.txt', 'test_files/b.txt']
    command = CatCommand(args)
    result = command.execute()
    assert "1\nHello, World!" == result.rstrip()


def test_cat_invalid_filename():
    # cat c.txt
    args = ['c.txt']
    command = CatCommand(args)
    result = command.execute()
    assert "" == result.rstrip()


def test_pwd():
    command = PwdCommand()
    result = command.execute()
    assert getcwd() == result.rstrip()


def test_wc_simple():
    # wc test_files/a.txt
    args = ['test_files/a.txt']
    command = WcCommand(args)
    result = command.execute()
    assert "       1       1       2 test_files/a.txt\n" == result


def test_wc_invalid_filename():
    # wc 123
    args = ['123']
    command = WcCommand(args)
    result = command.execute()
    assert "" == result.rstrip()
