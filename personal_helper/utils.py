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
