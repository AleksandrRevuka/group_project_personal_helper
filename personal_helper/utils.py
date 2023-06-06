"""utils"""

from typing import Callable


def format_phone_number(func: Callable[..., str]) -> Callable[..., str]:
    """Add '+' to phone's number"""
    def add_code_phone(phone: str) -> str:
        phone = func(phone)
        return ''.join('+' + phone)

    return add_code_phone


@format_phone_number
def sanitize_phone_number(phone: str) -> str:
    """Clean number"""
    return ''.join(number.strip().strip('(, ), -, +, x, .') for number in phone)


def transformation_commands(commands: list, target_command: str) -> dict:
    """
    The transformation_commands function takes a list of commands and a target command as input.
    It returns a dictionary with the keys being each command in the list, and the values being lists
    of booleans indicating whether or not that character in that position is correct for the target 
    command.

    :param commands: list: Store the commands that are to be transformed
    :param target_command: str: Create a dictionary of commands and their corresponding
    """
    result: dict = {}

    for command in commands:
        result[command] = []
        for index, char in enumerate(command):
            try:
                result[command].append(target_command[index] == char)
            except IndexError:
                pass

    return result


def get_close_command(commands_dict: dict) -> str | None:
    """
    The get_close_command function takes in a dictionary of commands and their respective values.
    It then iterates through the dictionary, counting how many True values each command has.
    The command with the most True values is returned as a string.

    :param commands_dict: dict: Store the commands and their values
    """
    max_true_count = 0
    max_true_element = None

    for element, values in commands_dict.items():
        true_count = values.count(True)

        if true_count > max_true_count:
            max_true_count = true_count
            max_true_element = element

    if max_true_element is None:
        return None

    return f"{max_true_element}"
