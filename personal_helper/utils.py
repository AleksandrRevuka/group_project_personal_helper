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


def get_validation_commands(commands: list, target_command: str) -> dict:
    result = {}
    
    for command in commands:
        result[command] = []
        for index, char in enumerate(command):
            try:
                result[command].append(target_command[index] == char)
            except IndexError:
                pass
        
    return result

def normalize_command(D: dict) -> str:
    
    max_true_count = 0
    max_true_element = None

    for element, values in D.items():
        true_count = values.count(True)

        if true_count > max_true_count:
            max_true_count = true_count
            max_true_element = element

    

    if max_true_element is None:
        return None
    
    return f"{max_true_element}"