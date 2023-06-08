"""
The address_book module provides classes for managing an address book and contact records.

This module defines the following classes:
    - AddressBook: A class representing an address book containing contact records.
    - Record: A class representing a contact record in the address book.
"""

import calendar
import re
import pickle
from datetime import datetime
from typing import Union, Any, List
from collections import UserDict


try:
    from .entities import Phone, User, Email
except ImportError:
    from entities import Phone, User, Email


class AddressBook(UserDict):
    """
    A class that represents an address book containing contact records.
    """

    def get_contact(self, name: str) -> "Record":
        """Returns the contact record for the given name."""
        return self.data[name]

    def add_record(self, record: "Record") -> None:
        """
        Adds a new contact record to the address book.
        """
        name = record.user.name
        if name:
            self.data[name] = record
            self.sort_addressbook()

    def delete_record(self, record_name: str) -> None:
        """
        Removes a contact record from the address book.
        """
        del self.data[record_name]

    def sort_addressbook(self) -> None:
        """
        The sort_addressbool function sorts the address book by name.
        """
        self.data = dict(sorted(self.data.items(), key=lambda x: x[0]))

    def search(self, criteria: str) -> Union[str, "AddressBook"]:
        """
        Searches the address book for contacts matching the given criteria.
        """
        serch_contacts = AddressBook()

        if criteria.isdigit():
            for record in self.data.values():
                for phone_number in record.phone_numbers:
                    if re.search(criteria, phone_number.subrecord.phone):
                        serch_contacts.add_record(record)

        else:
            for record in self.data.values():
                if re.search(criteria, record.user.name.lower()):
                    serch_contacts.add_record(record)

        if len(serch_contacts) == 0:
            return f"According to this '{criteria}' criterion, no matches were found"

        return serch_contacts

    def save_records_to_file(self, file_name: str) -> None:
        """
        Save the data in the address book to a binary file using pickle.
        """
        with open(file_name, "wb") as file:
            pickle.dump(self.data, file)

    def read_records_from_file(self, file_name: str) -> None:
        """
        Read data from a binary file using pickle and update the address book.
        """
        try:
            with open(file_name, "rb") as file:
                content = pickle.load(file)
                self.data.update(content)
        except FileNotFoundError as error:
            raise FileNotFoundError(f"File not found {file_name}") from error


class Record:
    """
    Record is a class that represents a contact record in a phone book.

    This class stores information about a contact, including user details, phone numbers, and emails.

    Attributes:
        user (User): The User object representing the user details of the contact.
        phone_numbers (List[Record.Subrecord]): A list of Subrecord objects representing the phone numbers of
        the contact.
        emails (List[Record.Subrecord]): A list of Subrecord objects representing the emails of the contact.

    Methods:
        add_phone_number: Adds a new phone number to the contact.

        add_email: Adds a new email to the contact.

        add_birthday: Adds a birthday date to the contact.

        days_to_birthday: Calculates the number of days until the next birthday of the contact.
    """

    class Subrecord:
        """
        Subrecord is a class representing a subrecord of a contact, such as a phone number or email.

        Attributes:
            name (List[str] | None): The name associated with the subrecord.
            subrecord (Any): The subrecord data.
        """

        def __init__(self, subrecord: Any):
            self.subrecord = subrecord

    def __init__(self, user: User):
        self.user = user
        self.phone_numbers: List["Record.Subrecord"] = []
        self.emails: List["Record.Subrecord"] = []

    def add_phone_number(self, phone_number: Phone) -> None:
        """
        Adds a new phone number to the contact.
        """
        subrecord_phone = self.Subrecord(phone_number)
        self.phone_numbers.append(subrecord_phone)

    def add_email(self, email: Email) -> None:
        """
        Adds a new email to the contact.
        """
        subrecord_email = self.Subrecord(email)
        self.emails.append(subrecord_email)

    def change_phone_number(
        self, old_phone_number: Phone, new_phone_number: Phone
    ) -> None:
        """
        Updates an existing phone number for the contact.
        """
        for phone_number in self.phone_numbers:
            if phone_number.subrecord == old_phone_number:
                phone_number.subrecord.phone = new_phone_number.phone
                return None

    def change_email(self, old_email: Email, new_email: Email) -> None:
        """
        Updates an existing email for the contact.
        """
        for email in self.emails:
            if email.subrecord == old_email:
                email.subrecord.email = new_email.email
                return None

    def delete_phone_number(self, phone_number: Phone) -> None:
        """
        Removes a phone number from the contact.
        """
        for i, number in enumerate(self.phone_numbers):
            if number.subrecord == phone_number:
                del self.phone_numbers[i]
                return None

    def delete_email(self, del_email: Email) -> None:
        """
        Removes a email from the contact.
        """
        for i, email in enumerate(self.emails):
            if email.subrecord == del_email:
                del self.emails[i]
                return None

    def add_birthday(self, birthday_date: str) -> None:
        """
        Add a birthday data to the contact.
        """
        birthday = datetime.strptime(birthday_date, "%d-%m-%Y").date()
        self.user.birthday_date = birthday

    def days_to_birthday(self) -> int | None:
        """
        Calculate the number of days to the next birthday.
        """

        birthday = self.user.birthday_date
        if birthday:
            # current_date = datetime(2020, 6, 5)
            # current_date = datetime(2020, 1, 5)
            current_date = datetime.now()
            has_29_february = False

            if birthday.day == 29 and birthday.month == 2:
                has_29_february = True

            if has_29_february and not calendar.isleap(current_date.year):
                birthday = birthday.replace(day=28)

            next_birthday = datetime(current_date.year, birthday.month, birthday.day)

            if (days_to_bd := (next_birthday - current_date).days) > 0:
                return days_to_bd
            else:
                next_year = current_date.year + 1

                if has_29_february:
                    if calendar.isleap(next_year):
                        next_birthday = next_birthday.replace(year=next_year, day=29)
                    else:
                        next_birthday = next_birthday.replace(year=next_year, day=28)
                else:
                    next_birthday = next_birthday.replace(year=next_year)

                days_to_bd = (next_birthday - current_date).days

                return days_to_bd
