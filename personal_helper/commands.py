"""
The main module consists of several functions that interact 
with an address book. Here is a brief description of each function:

load_contact_book(): This function loads the contact book from a file, creating an 
empty contact book if the file doesn't exist.

add_contact(contact_name: str, phone_number: str | None = None): This function adds 
a contact to the phone book. It validates the contact name and phone number (if provided) 
and saves the contact to the address book file.

print_contact(contact_name: str): This function prints the contact information 
of a given contact name, including phone number, email, birthday, and days to birthday.

delete_contact(contact_name: str): This function deletes a contact from the address book.

add_phone_number_to_contact(contact_name: str, phone_number: str): This function adds 
a phone number to an existing contact. It validates the phone number and ensures it doesn't 
already exist for the contact.

change_phone_number_contact(contact_name: str, new_phone_number: str, old_phone_number: 
str): This function changes the phone number of a contact. It validates the old and new 
phone numbers and updates the contact accordingly.

delete_phone_number_contact(contact_name: str, phone_number: str): This function deletes 
a phone number from a contact.

add_email_to_contact(contact_name: str, contact_email: str): This function adds an email 
to a contact. It validates the email and ensures it doesn't already exist for the contact.

change_email_contact(contact_name: str, contact_new_email: str, contact_old_email: str): 
This function changes the email of a contact. It validates the old and new emails and 
updates the contact accordingly.

delete_email_contact(contact_name: str, contact_email: str): This function deletes an email 
from a contact.

add_birthday_to_contact(contact_name: str, birthday_date: str): This function adds a birthday 
to a contact. It validates the birthday date and updates the contact accordingly.

search_contact(criteria: str): This function searches for a contact in the address book based 
on the specified criteria. It returns the matching contacts.

print_contacts(addressbook: AB = None): This function prints all contacts in the address book. 
If an address book is not provided, it loads the address book from the file.

birthday_in_next_days(days_interval: str): This function checks for contacts with birthdays 
in the next few days based on the specified days interval.

"""

import os.path
from pathlib import Path

try:
    from .utils import sanitize_phone_number
    from .validation import (
        name_validation,
        phone_validation,
        email_validation,
        birthday_date_validation,
        criteria_validation,
        check_name_in_address_book,
        check_name_not_in_address_book,
        check_phone_number_in_address_book,
        check_phone_number_not_in_address_book,
        check_email_in_address_book,
        check_email_not_in_address_book,
        check_path_address_to_sort_files_in_it,
        check_birthday_in_next_days,
    )
    from .constants import FILE
    from .address_book import Record, AddressBook as AB
    from .entities import Phone, User, Email
    from .print_table import TablePrinter
    from .sorting_files import SortingFiles
    from .notes import Notes

except ImportError:
    from utils import sanitize_phone_number
    from validation import (
        name_validation,
        phone_validation,
        email_validation,
        birthday_date_validation,
        criteria_validation,
        check_name_in_address_book,
        check_name_not_in_address_book,
        check_phone_number_in_address_book,
        check_phone_number_not_in_address_book,
        check_email_in_address_book,
        check_email_not_in_address_book,
        check_path_address_to_sort_files_in_it,
        check_birthday_in_next_days,
    )
    from constants import FILE
    from address_book import Record, AddressBook as AB
    from entities import Phone, User, Email
    from print_table import TablePrinter
    from sorting_files import SortingFiles
    from notes import Notes

def load_contact_book() -> AB:
    """
    The load_contact_book function loads the contact book from a file.
    If the file does not exist, it creates an empty contact book.
    """

    addressbook = AB()
    if os.path.exists(FILE):
        addressbook.read_records_from_file(FILE)
    return addressbook


def add_contact(contact_name: str, phone_number: str | None = None) -> None:
    """
    Adds a contact to the phone book.

    :param addressbook: AB: Pass the addressbook object to the function
    :param contact_name: str: Pass the name of the contact to be added
    :param phone_number: str: Verify the phone number
    """
    addressbook = load_contact_book()
    check_name_in_address_book(addressbook, contact_name)
    name_validation(contact_name)
    user = User(contact_name)
    contact = Record(user)
    if phone_number:
        phone_number = sanitize_phone_number(phone_number)
        phone_validation(phone_number)
        phone = Phone(phone_number)
        contact.add_phone_number(phone)
    addressbook.add_record(contact)
    addressbook.save_records_to_file(FILE)
    print(f"The contact '{contact_name}' has been added")


def print_contact(contact_name: str) -> None:
    """
    The print_contact function prints the contact information of a given contact name.

    :param addressbook: AB: Pass the addressbook object to the function
    :param contact_name: str: Specify the name of the contact to be printed
    """
    addressbook = load_contact_book()
    check_name_not_in_address_book(addressbook, contact_name)

    field_names = [
        "Contact Name",
        "Phone Number",
        "Email",
        "Birthday",
        "Days to Birthday",
    ]
    table = [field_names]

    contact = addressbook.get_contact(contact_name)
    phone_numbers: list | str = [
        number.subrecord.phone for number in contact.phone_numbers
    ]
    if not phone_numbers:
        phone_numbers = "-"

    emails: list | str = [email.subrecord.email for email in contact.emails]
    if not emails:
        emails = "-"
    birthday = (
        contact.user.birthday_date.strftime("%d-%m-%Y")
        if contact.user.birthday_date
        else "-"
    )
    day_to_birthday = contact.days_to_birthday() if contact.user.birthday_date else "-"
    table_row = [contact_name, phone_numbers, emails, birthday, day_to_birthday]
    table.append(table_row)
    table_ful = TablePrinter(table)
    table_ful.print_table()


def delete_contact(contact_name: str) -> None:
    """
    The delete_contact function deletes a contact from the addressbook.

    :param addressbook: AB: Pass the addressbook object to the function
    :param contact_name: str: Pass in the name of the contact to be deleted
    """
    addressbook = load_contact_book()
    check_name_not_in_address_book(addressbook, contact_name)

    addressbook.delete_record(contact_name)
    addressbook.save_records_to_file(FILE)
    print(f"The contact '{contact_name}' has been deleted.")


def add_phone_number_to_contact(contact_name: str, phone_number: str) -> None:
    """
    The add_phone_number_to_contact function adds a phone number to an existing contact.

    :param addressbook: AB: Pass the addressbook object to the function
    :param contact_name: str: Get the name of the contact that we want to add a phone number to
    :param phone_number: str: Pass the phone number to be added to the contact
    """
    addressbook = load_contact_book()
    phone_number = sanitize_phone_number(phone_number)
    phone_validation(phone_number)
    phone = Phone(phone_number)

    check_name_not_in_address_book(addressbook, contact_name)

    contact = addressbook.get_contact(contact_name)

    check_phone_number_in_address_book(contact, phone, contact_name)

    contact.add_phone_number(phone)
    addressbook.save_records_to_file(FILE)
    print(
        f"The phone number '{phone.phone}' has been successfully added to the '{contact_name}' contact."
    )


def change_phone_number_contact(
    contact_name: str, new_phone_number: str, old_phone_number: str
) -> None:
    """
    The change_phone_number_contact function is used to change the phone number of a contact in the address book.
        The function takes in an AddressBook object, a string representing the name of the contact whose phone number
        will be changed,and two strings representing both old and new phone numbers.

    :param addressbook: AB: Pass the addressbook object to the function
    :param contact_name: str: Specify the name of the contact that we want to change
    :param new_phone_number: str: Store the new phone number that will be used to replace the old one
    :param old_phone_number: str: Verify that the phone number exists in the contact's list of phone numbers
    """
    addressbook = load_contact_book()
    check_name_not_in_address_book(addressbook, contact_name)
    contact = addressbook.get_contact(contact_name)

    old_phone_number = sanitize_phone_number(old_phone_number)
    phone_validation(old_phone_number)
    old_phone = Phone(old_phone_number)
    check_phone_number_not_in_address_book(contact, old_phone, contact_name)

    new_phone_number = sanitize_phone_number(new_phone_number)
    phone_validation(new_phone_number)
    new_phone = Phone(new_phone_number)
    check_phone_number_in_address_book(contact, new_phone, contact_name)

    contact.change_phone_number(old_phone, new_phone)
    addressbook.add_record(contact)
    addressbook.save_records_to_file(FILE)
    print(
        f"The contact '{contact_name}' has been updated with the new phone number: {new_phone.phone}"
    )


def delete_phone_number_contact(contact_name: str, phone_number: str) -> None:
    """
    The delete_phone_number_contact function deletes a phone number from the contact.

    :param addressbook: AB: Pass the addressbook object to the function
    :param contact_name: str: Specify the name of the contact whose phone number is to be deleted
    :param phone_number: str: Identify the phone number that needs to be deleted
    """
    addressbook = load_contact_book()
    check_name_not_in_address_book(addressbook, contact_name)

    contact = addressbook.get_contact(contact_name)

    phone_number = sanitize_phone_number(phone_number)
    phone = Phone(phone_number)
    check_phone_number_not_in_address_book(contact, phone, contact_name)

    contact.delete_phone_number(phone)
    addressbook.save_records_to_file(FILE)
    print(
        f"The phone number '{phone.phone}' was successfully deleted from the '{contact_name}' contact."
    )


def add_email_to_contact(contact_name: str, contact_email: str) -> None:
    """
    The add_email_to_contact function adds an email to a contact in the address book.

    :param addressbook: AB: Pass in the addressbook object
    :param contact_name: str: Get the name of the contact you want to add an email to
    :param email: str: Pass the email address to be added to the contact
    """
    addressbook = load_contact_book()
    contact_email = contact_email.lower()
    check_name_not_in_address_book(addressbook, contact_name)

    contact = addressbook.get_contact(contact_name)

    email_validation(contact_email)
    email = Email(contact_email)

    check_email_in_address_book(contact, email, contact_name)

    contact.add_email(email)
    addressbook.save_records_to_file(FILE)
    print(
        f"The email '{email.email}' has been successfully added to the '{contact_name}' contact."
    )


def change_email_contact(
    contact_name: str, contact_new_email: str, contact_old_email: str
) -> None:
    """
    The change_email_contact function takes in an addressbook, a contact name,
    a new email and an old email. It then checks if the contact name is not in the
    address book. If it isn't then it will check if the old email is not in that
    contact's list of emails. If it isn't then we verify that the new_email is valid
    and create a new Email object with this value as its parameter. We also check to see
    if this new_email already exists within our contacts list of emails and throw an error
    message accordingly.

    :param addressbook: AB: Pass in the addressbook object
    :param contact_name: str: Get the contact name from the user
    :param new_email: str: Store the new email that will be added to the contact
    :param old_email: str: Specify the email that is to be changed
    """
    addressbook = load_contact_book()
    contact_new_email = contact_new_email.lower()
    contact_old_email = contact_old_email.lower()
    check_name_not_in_address_book(addressbook, contact_name)

    contact = addressbook.get_contact(contact_name)

    old_email = Email(contact_old_email)
    check_email_not_in_address_book(contact, old_email, contact_name)

    email_validation(contact_new_email)
    new_email = Email(contact_new_email)

    check_email_in_address_book(contact, new_email, contact_name)

    contact.change_email(old_email, new_email)
    addressbook.save_records_to_file(FILE)
    print(
        f"The contact '{contact_name}' has been updated with the new email: {new_email.email}"
    )


def delete_email_contact(contact_name: str, contact_email: str) -> None:
    """
    The delete_email_contact function deletes an email from a contact.

    :param addressbook: AB: Pass in the addressbook object
    :param contact_name: str: Get the contact name from the user
    :param email: str: Get the email address that will be deleted from the contact
    """
    addressbook = load_contact_book()
    contact_email = contact_email.lower()
    check_name_not_in_address_book(addressbook, contact_name)

    contact = addressbook.get_contact(contact_name)
    email = Email(contact_email)

    check_email_not_in_address_book(contact, email, contact_name)

    contact.delete_email(email)
    addressbook.save_records_to_file(FILE)
    print(
        f"The email '{email.email}' was successfully deleted from the '{contact_name}' contact."
    )


def add_birthday_to_contact(contact_name: str, birthday_date: str) -> None:
    """
    The add_birthday_to_contact function adds a birthday to the contact.

    :param addressbook: AB: Specify the addressbook object that is being used
    :param contact_name: str: Identify the contact to add a birthday to
    :param birthday_date: str: Verify that the birthday date is valid
    """
    addressbook = load_contact_book()
    check_name_not_in_address_book(addressbook, contact_name)

    contact = addressbook.get_contact(contact_name)

    birthday_date_validation(birthday_date)
    contact.add_birthday(birthday_date)

    addressbook.add_record(contact)
    addressbook.save_records_to_file(FILE)
    print(
        f"The birthday '{birthday_date}' has been added to the '{contact_name}' contact."
    )


def serch_contact(criteria: str) -> None:
    """
    The serch_contact function searches for a contact in the address book.

    :param addressbook: AB: Specify the type of the parameter
    :param criteria: str: Specify the search criteria
    """
    addressbook = load_contact_book()
    criteria = criteria.lower()
    criteria_validation(criteria)

    result = addressbook.search(criteria)

    if isinstance(result, AB):
        print_contacts(result)
    else:
        print(result)

    print(f"{len(result)} contacts were found based on your search criteria!")


def print_contacts(addressbook: AB = None) -> None:
    """
    The print_all_contacts function prints all the contacts in the addressbook.
        It takes an AddressBook object as a parameter and returns nothing.

    :param addressbook: AB: Pass the addressbook object to the function
    """
    if not addressbook:
        addressbook = load_contact_book()
    field_names = [
        "Contact Name",
        "Phone Number",
        "Email",
        "Birthday",
        "Days to Birthday",
    ]
    table = [field_names]
    for contact in addressbook.values():
        contact_name = contact.user.name
        phone_numbers: list | str = [
            number.subrecord.phone for number in contact.phone_numbers
        ]
        if not phone_numbers:
            phone_numbers = "-"

        emails: list | str = [email.subrecord.email for email in contact.emails]
        if not emails:
            emails = "-"

        birthday = (
            contact.user.birthday_date.strftime("%d-%m-%Y")
            if contact.user.birthday_date
            else "-"
        )
        day_to_birthday = (
            contact.days_to_birthday() if contact.user.birthday_date else "-"
        )

        table_row = [contact_name, phone_numbers, emails, birthday, day_to_birthday]

        table.append(table_row)
    table_ful = TablePrinter(table)
    table_ful.print_table()


def birthday_in_next_days(days_interval: str) -> None:
    """
    The birthday_in_next_days function takes a string as an argument and returns None.
    The function checks if the input is valid, then loads the address book from file.
    It iterates through each contact in the address book and checks if they have a birthday date set. If so,
    it calculates how many days are left until their birthday using days_to_birthday() method of User class.
    If this number is less than or equal to user's input (days interval), it adds that contact to
    contacts_with_birthday dictionary which will be printed at the end.

    :param days_interval: str: Specify the number of days from today to search for birthdays
    """

    check_birthday_in_next_days(days_interval)

    contacts_with_birthday = AB()
    addressbook = load_contact_book()

    for contact in addressbook.values():
        if contact.user.birthday_date:
            days_to_birthday = contact.days_to_birthday()
            if days_to_birthday <= int(days_interval):
                contacts_with_birthday.add_record(contact)
    if len(contacts_with_birthday) == 0:
        print(f"No users have a birthday within the next {days_interval} days.")
    else:
        print_contacts(contacts_with_birthday)


def run_sorting_files(address: str) -> None:
    """
    The run_sorting_files function sorts files in a given directory.
        It takes the address of the directory as an argument and returns None.
        The function checks if the path is valid, creates an instance of SortingFiles class,
        calls its methods to sort files by their extensions and remove empty folders.

    :param address: str: Get the address of the directory that we want to sort
    """
    path = Path(address)
    check_path_address_to_sort_files_in_it(path)

    sorting_files = SortingFiles(path)
    sorting_files.files_addresses()
    sorting_files.sort_extensions()
    sorting_files.removing_files()
    sorting_files.del_empty_folders()
    print(f"Directory {address} has been sorted succesfully!")


def add_note_to_data(tags: list, text: str = "") -> None:
    """
    The add_note_to_data function adds notes with tags. If no tag is specified, a default tag is assigned

    :param tags: list: Specify the tags that will be assigned to the note
    :param text: Specify the text of the note
    """
    note = Notes()
    note.load()
    note.add_note(tags, text)
    note.save()


def find_note(key_word: str = "") -> None:
    """
    The find_note function searches for a note by keyword/letter/symbol.
    The search is conducted by tags and by the text of the notes at the same time.

    :param key_word: str: Specify the keyword to search for
    """
    note = Notes()
    note.load()
    note.find(key_word)
    print("The search is over!")


def show_all_notes() -> None:
    """
    The show_all_notes function is used to display all the notes in the Notes.txt file.
    The function first loads all of the notes from Notes.txt into a list, then sorts them by date and time,
    and finally displays them on screen.
    """

    note = Notes()
    note.load()
    note.show_all_sorted_notes()
    note.save()


def delete_note(tag: str) -> None:
    """
    The delete_note function deletes a note from the notes.txt file.

    :param tag: str: Specify which note to delete
    """

    note = Notes()
    note.load()
    note.del_notes(tag)
    note.save()


def edit_note(tag: str, new_tag: list, new_text: str) -> None:
    """
    The edit_note function allows the user to edit a note.
    The function takes in three parameters: tag, new_tag, and new_text.
    Tag is the name of the note that will be edited. New_tag is a list of tags that will replace old ones for this note.
    New text is what replaces old text for this note.

    :param tag: str: Find the note that is to be edited
    :param new_tag: list: Allow the user to add multiple tags to a note
    :param new_text: str: Change the text of a note
    """

    note = Notes()
    note.load()
    note.edit_notes(tag, new_tag, new_text)
    note.save()
