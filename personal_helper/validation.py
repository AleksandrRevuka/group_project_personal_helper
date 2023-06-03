"""validation"""

import re
from string import digits
from datetime import datetime

from error import input_error
from constants import LETTERS, NAME_RANGE, PHONE_RANGE
from address_book import Record, AddressBook as AB
from entities import Phone, Email


@input_error
def verify_name(name: str) -> None:
    """Verifies that the input string `name` is a valid name for a contact."""

    if not isinstance(name, str):
        raise TypeError(
            f"Name must be a string, but got {type(name).__name__}")

    if len(name.strip(LETTERS)) != 0:
        raise TypeError(
            f"Contact's name can only contain letters, but got '{name.title()}'")

    if len(name) not in NAME_RANGE:
        raise ValueError(
            f"Name length must be between {NAME_RANGE[0]} and {NAME_RANGE[-1]}, but got '{name.title()}'")


@input_error
def verify_phone(phone: str) -> None:
    """Verifies a phone number."""

    if len(phone.strip(digits + '+')) != 0:
        raise TypeError(
            f"Contact's phone can only contain digits, but got '{phone}'")

    if len(phone) not in PHONE_RANGE:
        raise ValueError(
            f"Contact's phone must be between 11 and 16 numbers, but got '{phone}'")


@input_error
def verify_birthday_date(birthday_date: str) -> None:
    """Verifies a birthday data."""
    try:
        birthday = datetime.strptime(birthday_date, '%d-%m-%Y')
    except ValueError as error:
        raise ValueError(
            f"Incorrect date format: '{birthday_date}', should be in the format DD-MM-YYYY") from error

    if birthday >= datetime.now():
        raise ValueError(
            f"Birthday '{birthday.date()}' must be in the past")


@input_error
def verify_email(email: str) -> None:
    """Verifies an email address."""
    pattern = r"[a-zA-Z][a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    if not re.match(pattern, email):
        raise ValueError(f"Invalid '{email}' email address.")


@input_error
def verify_criteria(criteria: str) -> None:
    """
    The verify_criteria function is used to verify that the criteria entered by the user
    is only numbers or letters.  If it is not, then a ValueError exception will be raised.
    """
    if not criteria.isdigit() and not criteria.isalpha():
        raise ValueError(
            f"Criteria '{criteria}' must be only numbers or letters")


@input_error
def check_name_in_address_book(address_book: AB, name: str) -> None:
    """
    The check_name_in_address_book function checks if a name is already in the address book.
        If it is, then an error message will be raised.
    """
    if name in address_book:
        raise ValueError(
            f"The contact '{name.title()}' already exists in the address book.")


@input_error
def check_name_not_in_address_book(address_book: AB, name: str) -> None:
    """
    The check_name_not_in_address_book function checks if the name is already in the address book.
        If it is, then a ValueError exception will be raised with an error message explaining that
        the contact already exists in the address book.
    """
    if name not in address_book:
        raise KeyError(f"The contact '{name.title()}' was not found.")


@input_error
def check_phone_number_in_address_book(contact: Record, phone: Phone, contact_name: str) -> None:
    """
    The check_phone_number_in_address_book function checks if a phone number already exists in the address book.
        If it does, then an error is raised.
    """
    if phone in [phone_number.subrecord for phone_number in contact.phone_numbers]:
        raise ValueError(
            f"The phone number '{phone.phone}' already exists in the '{contact_name.title()}' contact.")


@input_error
def check_phone_number_not_in_address_book(contact: Record,
                                           phone: Phone,
                                           contact_name: str) -> None:
    """
    The check_phone_number_not_in_address_book function checks that the phone number to be updated is in the address book.
        If it is not, then an error message will be raised.
    """
    if phone not in [phone_number.subrecord for phone_number in contact.phone_numbers]:
        raise ValueError(
            f"Contact's phone '{phone.phone}' was not found in the '{contact_name.title()}' contact.")


@input_error
def check_email_in_address_book(contact: Record, email: Email, contact_name: str) -> None:
    """
    The check_email_in_address_book function checks if the email already exists in the contact's emails.
        If it does, then a ValueError is raised with an error message explaining that this email already exists.
    """
    if email in [email.subrecord for email in contact.emails]:
        raise ValueError(
            f"The contact's email '{email.email}' already exists in this '{contact_name.title()}' contact.")


@input_error
def check_email_not_in_address_book(contact: Record, email: Email, contact_name: str) -> None:
    """
    The check_email_not_in_address_book function checks to see if the email is in the contact's list of emails.
    If it is not, then a ValueError exception will be raised.
    """
    if email not in [email.subrecord for email in contact.emails]:
        raise ValueError(
            f"Contact's email '{email.email}' was not found in the '{contact_name.title()}' contact.")
