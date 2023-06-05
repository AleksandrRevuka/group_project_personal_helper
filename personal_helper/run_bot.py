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
from constants import ADDRESSBOOK_COMMANDS
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
    print_contact,
    serch_contact
)
from utils import transformation_commands, get_close_command

def add_parser(arguments: str) -> argparse.Namespace:
    """
    The build_parser function takes a string of arguments and returns an argparse.Namespace object.
    The Namespace object contains the values of all the arguments passed in as attributes, which 
    can be accessed by name.
    """
    parser = argparse.ArgumentParser(prog='add', description='add', usage='\nadd -h\nadd -n <name> -p <phone>')
    parser.add_argument("-n", dest="name", help='Contact name')
    parser.add_argument("-p", dest="phone", help='Number of phone')
    args = parser.parse_args(arguments.split())
    return args


def change_parser(arguments: str) -> argparse.Namespace:
    """
    The build_parser function takes a string of arguments and returns an argparse.Namespace object.
    The Namespace object contains the values of all the arguments passed in as attributes, which 
    can be accessed by name.
    """
    parser = argparse.ArgumentParser(prog='change', description='change contact or contact data')
    parser.add_argument("-n", dest="name", help='Contact name')
    parser.add_argument("-p", dest="phone", help='Number of phone')
    parser.add_argument("-e", dest="email", help='email')
    parser.add_argument("-b", dest="birthday", help='Date of birth in format dd-mm-yyyy')
    parser.add_argument("-r", dest="replace", help='This argument use only after -p or -e')
    args = parser.parse_args(arguments.split())
    return args


def del_parser(arguments: str) -> argparse.Namespace:
    """
    The build_parser function takes a string of arguments and returns an argparse.Namespace object.
    The Namespace object contains the values of all the arguments passed in as attributes, which 
    can be accessed by name.
    """
    parser = argparse.ArgumentParser(prog='del', description='delete contact or contact data')
    parser.add_argument("-n", dest="name", help='Contact name')
    parser.add_argument("-p", dest="phone", help='Number of phone')
    parser.add_argument("-e", dest="email", help='email')
    args = parser.parse_args(arguments.split())
    return args


def show_parser(arguments: str) -> argparse.Namespace:
    """
    The build_parser function takes a string of arguments and returns an argparse.Namespace object.
    The Namespace object contains the values of all the arguments passed in as attributes, which 
    can be accessed by name.
    """
    parser = argparse.ArgumentParser(prog='show', description='dicplay contact data')
    parser.add_argument("-a", dest="show", help='Use show -a all or show -a <contact_name>')
    args = parser.parse_args(arguments.split())
    return args


def search_parser(arguments: str) -> argparse.Namespace:
    """
    The build_parser function takes a string of arguments and returns an argparse.Namespace object.
    The Namespace object contains the values of all the arguments passed in as attributes, which 
    can be accessed by name.
    """
    parser = argparse.ArgumentParser(prog='search', description='search')
    parser.add_argument("-s", dest="search", help='Use search -s <key word>')
    args = parser.parse_args(arguments.split())
    return args


def note_parser(arguments: str) -> argparse.Namespace:
    """
    The build_parser function takes a string of arguments and returns an argparse.Namespace object.
    The Namespace object contains the values of all the arguments passed in as attributes, which 
    can be accessed by name.
    """
    parser = argparse.ArgumentParser(prog='note', description='note')
    parser.add_argument("-a", dest="add", help='add new note')
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
    if command_elements[0] == 'add':
        parsed_args = add_parser(arguments)
        return command_elements[0], parsed_args
    elif command_elements[0] == 'change':
        parsed_args = change_parser(arguments)
        return command_elements[0], parsed_args
    elif command_elements[0] == 'del':
        parsed_args = del_parser(arguments)
        return command_elements[0], parsed_args
    elif command_elements[0] == 'show':
        parsed_args = show_parser(arguments)
        return command_elements[0], parsed_args
    elif command_elements[0] == 'search':
        parsed_args = search_parser(arguments)
        return command_elements[0], parsed_args
    elif command_elements[0] == 'note':
        parsed_args = note_parser(arguments)
        return command_elements[0], parsed_args


def addressbook_controller(command: str, arguments: dict):
    if command == 'add':
        add_contact(arguments.name, arguments.phone)
    elif command == 'change':
        if arguments.phone and not arguments.replace:
            add_phone_number_to_contact(arguments.name, arguments.phone)
        elif arguments.phone and arguments.replace:
            change_phone_number_contact(arguments.name, arguments.replace, arguments.phone)
        elif arguments.email and not arguments.replace:
            add_email_to_contact(arguments.name, arguments.email)
        elif arguments.email and arguments.replace:
            change_email_contact(arguments.name, arguments.replace, arguments.email)
        elif arguments.birthday:
            add_birthday_to_contact(arguments.name, arguments.birthday)
    elif command == 'del':
        if arguments.name and arguments.phone:
            delete_phone_number_contact(arguments.name, arguments.phone)
        elif arguments.name and arguments.email:
            delete_email_contact(arguments.name, arguments.email)
        elif arguments.name and not arguments.email and not arguments.phone:
            delete_contact(arguments.name)
    elif command == 'show':
        if arguments.show == 'all':
            print_contacts()
        elif arguments.show:
            print_contact(arguments.show)
    elif command == 'search':
        serch_contact(arguments.search)
        
        
def nete_controller(command: str, arguments: dict):
    pass
  

def main() -> None:
    """
    The main function of the program.
    """
    user_command = ' '.join(argv[1:])
    info_message = 'Use command:\nadd\nchange\ndel\nshow\nsearch\n\nDetail about command:\n[command] -h'
    if not user_command or user_command == '-h':
        print(info_message)
        return
    command, arguments = command_parser(user_command)

    if command in ADDRESSBOOK_COMMANDS and arguments:
        addressbook_controller(command, arguments)
    elif command == 'note' and arguments:
        pass
    else:
        print(f'Command *{command}* invalid or used without arguments! Try again or use help.')
        print(info_message)


if __name__ == '__main__':
    main()
