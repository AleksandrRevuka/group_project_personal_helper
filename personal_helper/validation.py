"""validation"""

import re
from string import digits
from datetime import datetime
import os
from pathlib import Path

try:
    from .error import input_error
    from .constants import LETTERS, NAME_RANGE, PHONE_RANGE
    from .address_book import Record, AddressBook as AB
    from .entities import Phone, Email
except ImportError:
    from error import input_error
    from constants import LETTERS, NAME_RANGE, PHONE_RANGE
    from address_book import Record, AddressBook as AB
    from entities import Phone, Email


@input_error
def name_validation(name: str) -> None:
    """
    The name_validation function checks if the name is a string, and if it contains only letters.
    It also checks that the length of the name is between 2 and 30 characters.
    """

    if not isinstance(name, str):
        raise TypeError(f"Name must be a string, but got {type(name).__name__}")

    if len(name.strip(LETTERS)) != 0:
        raise TypeError(
            f"Contact's name can only contain letters, but got '{name.title()}'"
        )

    if len(name) not in NAME_RANGE:
        raise ValueError(
            f"Name length must be between {NAME_RANGE[0]} and {NAME_RANGE[-1]}, but got '{name}'"
        )


@input_error
def phone_validation(phone: str) -> None:
    """
    The phone_validation function checks if the phone number is valid.
        It raises a TypeError if the phone number contains anything other than digits and '+'.
        It raises a ValueError if the length of the phone number is not between 11 and 16 numbers.
    """
    if len(phone.strip(digits + "+")) != 0:
        raise TypeError(f"Contact's phone can only contain digits, but got '{phone}'")

    if len(phone) not in PHONE_RANGE:
        raise ValueError(
            f"Contact's phone must be between 11 and 16 numbers, but got '{phone}'"
        )


@input_error
def birthday_date_validation(birthday_date: str) -> None:
    """
    The birthday_date_validation function takes a string as an argument and checks if it is in the correct format.
    If not, it raises a ValueError exception. If the date is in the future, another ValueError exception will be raised.
    """

    try:
        birthday = datetime.strptime(birthday_date, "%d-%m-%Y")
    except ValueError as error:
        raise ValueError(
            f"Incorrect date format: '{birthday_date}', should be in the format DD-MM-YYYY"
        ) from error

    if birthday >= datetime.now():
        raise ValueError(f"Birthday '{birthday.date()}' must be in the past")


@input_error
def email_validation(email: str) -> None:
    """
    The email_validation function takes in a string and checks if it is a valid email address.
    It does this by using the re module to match the inputted string with a pattern that represents
    a valid email address. If there is no match, then an error message will be raised.
    """

    pattern = r"[a-zA-Z][a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    if not re.match(pattern, email):
        raise ValueError(f"Invalid '{email}' email address.")


@input_error
def criteria_validation(criteria: str) -> None:
    """
    The criteria_validation function is used to verify that the criteria entered by the user
    is only numbers or letters.  If it is not, then a ValueError exception will be raised.
    """
    if not criteria.isdigit() and not criteria.isalpha():
        raise ValueError(f"Criteria '{criteria}' must be only numbers or letters")


@input_error
def check_name_in_address_book(address_book: AB, name: str) -> None:
    """
    The check_name_in_address_book function checks if a name is already in the address book.
        If it is, then an error message will be raised.
    """
    if name in address_book:
        raise ValueError(f"The contact '{name}' already exists in the address book.")


@input_error
def check_name_not_in_address_book(address_book: AB, name: str) -> None:
    """
    The check_name_not_in_address_book function checks if the name is already in the address book.
        If it is, then a ValueError exception will be raised with an error message explaining that
        the contact already exists in the address book.
    """
    if name not in address_book:
        raise KeyError(f"The contact '{name}' was not found.")


@input_error
def check_phone_number_in_address_book(
    contact: Record, phone: Phone, contact_name: str
) -> None:
    """
    The check_phone_number_in_address_book function checks if a phone number already exists in the address book.
        If it does, then an error is raised.
    """
    if phone in [phone_number.subrecord for phone_number in contact.phone_numbers]:
        raise ValueError(
            f"The phone number '{phone.phone}' already exists in the '{contact_name}' contact."
        )


@input_error
def check_phone_number_not_in_address_book(
    contact: Record, phone: Phone, contact_name: str
) -> None:
    """
    The check_phone_number_not_in_address_book function checks that the phone number to be updated is in the address book.
        If it is not, then an error message will be raised.
    """
    if phone not in [phone_number.subrecord for phone_number in contact.phone_numbers]:
        raise ValueError(
            f"Contact's phone '{phone.phone}' was not found in the '{contact_name}' contact."
        )


@input_error
def check_email_in_address_book(
    contact: Record, email: Email, contact_name: str
) -> None:
    """
    The check_email_in_address_book function checks if the email already exists in the contact's emails.
        If it does, then a ValueError is raised with an error message explaining that this email already exists.
    """
    if email in [email.subrecord for email in contact.emails]:
        raise ValueError(
            f"The contact's email '{email.email}' already exists in this '{contact_name}' contact."
        )


@input_error
def check_email_not_in_address_book(
    contact: Record, email: Email, contact_name: str
) -> None:
    """
    The check_email_not_in_address_book function checks to see if the email is in the contact's list of emails.
    If it is not, then a ValueError exception will be raised.
    """
    if email not in [email.subrecord for email in contact.emails]:
        raise ValueError(
            f"Contact's email '{email.email}' was not found in the '{contact_name}' contact."
        )


@input_error
def check_path_address_to_sort_files_in_it(path: Path) -> None:
    """Checks if the path (for sorting files) exists and if it points to a folder"""
    if not path.exists():
        raise ValueError("The way is not exists!")
    if os.path.isfile(path):
        raise ValueError("The path points to a file! Must point to a folder!")


@input_error
def check_birthday_in_next_days(days_interval: str) -> None:
    """
    The check_birthday_in_next_days function checks if the days_interval parameter is a digit.
    If it's not, then an exception is raised.
    """
    try:
        int(days_interval)
    except ValueError as error:
        raise ValueError("The days parameter should be a digit.") from error
