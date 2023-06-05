"""
This module provides a command-line interface for managing a contact book. It allows users to perform various operations
such as adding contacts, modifying contact information, deleting contacts, and displaying contact details.

The module consists of the following components:
- `address_book`: Contains the `AddressBook` class that represents the contact book.
- `constants`: Defines constants used in the module.
- `commands`: Provides functions for executing different commands on the contact book.
- `build_parser`: Defines a function for parsing command-line arguments using `argparse`.
- `command_parser`: Implements a function for parsing user commands and extracting command names and arguments.
- `load_contact_book`: Loads the contact book from a file or creates an empty contact book if the file doesn't exist.
- `main`: The main function that processes user commands and executes the corresponding operations.

To run the module, execute the script `run_bot.py` with appropriate command-line arguments.

Example usage:
    $ python run_bot.py add -n John -p 380634567890
    $ python run_bot.py change -n John -p 380991234567 -r 380634567890
    $ python run_bot.py del -n John
"""



import argparse
from sys import argv
import os.path

from address_book import AddressBook
from constants import FILE, LIST_COMMANDS
from commands import (
    add_contact,
    add_phone_number_to_contact,
    change_phone_number_contact,
    add_email_to_contact,
    change_email_contact,
    add_birthday_to_contact,
    delete_phone_number_contact,
    delete_email_contact,
    delete_contact,
    print_contacts,
    print_contact
)
from utils import transformation_commands, get_close_command


def build_parser(arguments: str) -> argparse.Namespace:
    """
    The build_parser function takes a string of arguments and returns an argparse.Namespace object.
    The Namespace object contains the values of all the arguments passed in as attributes, which 
    can be accessed by name.
    """
    parser = argparse.ArgumentParser(description="Contact book")
    parser.add_argument("-n", dest="name")
    parser.add_argument("-p", dest="phone")
    parser.add_argument("-e", dest="email")
    parser.add_argument("-b", dest="birthday")
    parser.add_argument("-r", dest="replace")
    parser.add_argument("-d", dest="delete_phone")
    parser.add_argument("-a", dest="show")
    parser.add_argument("-s", dest="search")
    args = parser.parse_args(arguments.split())
    return args


def command_parser(user_command: str) -> tuple[str, argparse.Namespace | None]:
    """
    The command_parser function takes a user command as input and returns the
    command name and arguments. The function first splits the user command into
    a list of elements, where each element is separated by a space. If there are no
    arguments, then it returns only the command name (the first element in the list). 
    If there are arguments, then it uses argparse to parse them into an object that can be used later.
    """
    command_elements = user_command.split(' ')
    if len(command_elements) < 2:
        arguments = None
        return command_elements[0], arguments

    arguments = user_command.split(' ', 1)[1]
    parsed_args = build_parser(arguments)
    return command_elements[0], parsed_args


def load_contact_book() -> AddressBook:
    """
    The load_contact_book function loads the contact book from a file.
    If the file does not exist, it creates an empty contact book.
    """
    contact_book = AddressBook()
    if os.path.exists(FILE):
        contact_book.read_records_from_file(FILE)
    return contact_book


def main() -> None:
    """
    The main function of the program.
    """
    contact_book = load_contact_book()
    user_command = ' '.join(argv[1:])
    command, arguments = command_parser(user_command)
    

    if not arguments:

        print('Commands without arguments or error')
    else:
        user_input = ''

        if command not in LIST_COMMANDS:
            temp_command = transformation_commands(get_close_command(LIST_COMMANDS, command))
            if temp_command is not None:
                user_input = input(f'Did you mean command [{temp_command}]? y/n -> ')
            else:
                print(f'Command [{command}] is not found!')

        if user_input == 'y':
            command = temp_command
    
        if command == 'add':
            add_contact(contact_book, arguments.name, arguments.phone)
        elif command == 'change':
            if arguments.phone and not arguments.replace:
                add_phone_number_to_contact(contact_book, arguments.name, arguments.phone)
            elif arguments.phone and arguments.replace:
                change_phone_number_contact(contact_book, arguments.name, arguments.replace, arguments.phone)
            elif arguments.email and not arguments.replace:
                add_email_to_contact(contact_book, arguments.name, arguments.email)
            elif arguments.email and arguments.replace:
                change_email_contact(contact_book, arguments.name, arguments.replace, arguments.email)
            elif arguments.birthday:
                add_birthday_to_contact(contact_book, arguments.name, arguments.birthday)
        elif command == 'del':
            if arguments.name and arguments.phone:
                delete_phone_number_contact(contact_book, arguments.name, arguments.phone)
            elif arguments.name and arguments.email:
                delete_email_contact(contact_book, arguments.name, arguments.email)
            elif arguments.name and not arguments.email and not arguments.phone:
                delete_contact(contact_book, arguments.name)
        elif command == 'show':
            if arguments.show == 'all':
                print_contacts(contact_book)
            elif arguments.show:
                print_contact(contact_book, arguments.show)

        print('We have arguments')
        print(arguments)


if __name__ == '__main__':
    main()
