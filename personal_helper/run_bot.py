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
from constants import (
    ADDRESSBOOK_COMMANDS, 
    LIST_COMMANDS,
    INFO_MESSAGE
)

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
    serch_contact,
    run_sorting_files,
    edit_note,
    delete_note,
    show_all_notes,
    find_note,
    add_note_to_data,
    birthday_in_next_days
)
from utils import transformation_commands, get_close_command

def add_parser(arguments: str) -> argparse.Namespace:
    """
    The build_parser function takes a string of arguments and returns an argparse.Namespace object.
    The Namespace object contains the values of all the arguments passed in as attributes, which 
    can be accessed by name.
    """
    usage_info = '\nadd -h\nadd -n <name> -p <phone>'
    parser = argparse.ArgumentParser(prog='add', description='Create new contact', usage=usage_info)
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
    usage_info = '\nchange -h\nchange -n <name> -p <phone> -e\nchange -n <name> -p <phone> -r <phone>\nchange -n <name> -e <email>\nchange -n <name> -e <emeil> -r <emeil>\nchange -n <name> -b <birthday>'
    parser = argparse.ArgumentParser(prog='change', description='change contact or contact data', usage=usage_info)
    parser.add_argument("-n", dest="name", help='Contact name')
    parser.add_argument("-p", dest="phone", help='Phone Number')
    parser.add_argument("-e", dest="email", help='User Email')
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
    usage_info = '\ndel -h\ndel -n <name>\ndel -n <name> -p <phone>\ndel -n <name> -e <emeil>\ndel-n <name> -b <birthday>'
    parser = argparse.ArgumentParser(prog='del', description='delete contact or contact data', usage=usage_info)
    parser.add_argument("-n", dest="name", help='Contact name')
    parser.add_argument("-p", dest="phone", help='Phone Number')
    parser.add_argument("-e", dest="email", help='User Email')
    parser.add_argument("-b", dest="birthday", help='Date of birth in format dd-mm-yyyy')
    args = parser.parse_args(arguments.split())
    return args


def show_parser(arguments: str) -> argparse.Namespace:
    """
    The build_parser function takes a string of arguments and returns an argparse.Namespace object.
    The Namespace object contains the values of all the arguments passed in as attributes, which 
    can be accessed by name.
    """
    usage_info = '\nshow -h\nshow -a all\nshow -a <name>'
    parser = argparse.ArgumentParser(prog='show', description='display contact data', usage=usage_info)
    parser.add_argument("-a", dest="show", help='Use show -a <all> or show -a <name>')
    args = parser.parse_args(arguments.split())
    return args


def search_parser(arguments: str) -> argparse.Namespace:
    """
    The build_parser function takes a string of arguments and returns an argparse.Namespace object.
    The Namespace object contains the values of all the arguments passed in as attributes, which 
    can be accessed by name.
    """
    usage_info = '\nsearch -h\nsearch -s <key_word>'
    parser = argparse.ArgumentParser(prog='search', description='search', usage=usage_info)
    parser.add_argument("-s", dest="search", help='Search by keywords -s <key word>')
    args = parser.parse_args(arguments.split())
    return args


def birth_parser(arguments: str) -> argparse.Namespace:
    """
    The build_parser function takes a string of arguments and returns an argparse.Namespace object.
    The Namespace object contains the values of all the arguments passed in as attributes, which 
    can be accessed by name.
    """
    usage_info = '\nbirth -h\nbirth -d <days>'
    parser = argparse.ArgumentParser(prog='birth', description='birth', usage=usage_info)
    parser.add_argument("-d", dest="days", help='Range of days')
    args = parser.parse_args(arguments.split())
    return args


def sort_parser(arguments: str) -> argparse.Namespace:
    """
    The build_parser function takes a string of arguments and returns an argparse.Namespace object.
    The Namespace object contains the values of all the arguments passed in as attributes, which 
    can be accessed by name.
    """
    usage_info = '\nsort -h\nsort -d sort -d <"Path">'
    parser = argparse.ArgumentParser(prog='sort', description='sort', usage=usage_info)
    parser.add_argument("-d", dest="directory", help='Path to directory')
    args = parser.parse_args(arguments.split())
    return args


def note_parser(arguments: str) -> argparse.Namespace:
    """
    The build_parser function takes a string of arguments and returns an argparse.Namespace object.
    The Namespace object contains the values of all the arguments passed in as attributes, which 
    can be accessed by name.
    """

    usage_info = '\nnote -h\note -a <tag> -n <text note>\nnote -f <tag>\nnote -t <old_tag> -r <new_tag> -n\nnote -s all\nnote -d <tag>\nnote -n <note>\nnote -r <replace>'
    parser = argparse.ArgumentParser(prog='note', description='note',usage=usage_info)
    parser.add_argument("-a", dest="add", nargs='+', help='Add new note')
    parser.add_argument("-f", dest="find", help='Find note')
    parser.add_argument("-t", dest="tag", help='Tag')
    parser.add_argument("-s", dest="show", help='Show all note')
    parser.add_argument("-d", dest="delete", help='Delete notes')
    parser.add_argument("-n", dest="note", type=str, nargs='+', help='Note text')
    parser.add_argument("-r", dest="replace", nargs='+', help='New tag')
    args = parser.parse_args(arguments.split())
    if args.note:
        string = ''
        for element in args.note:
            string += element + ' '
        args.note = string 
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
    if command_elements[0] not in LIST_COMMANDS:
        temp_command = get_close_command(transformation_commands(LIST_COMMANDS, command_elements[0]))
        if temp_command:
            user_input = input(f'Did you mean command [{temp_command}]? y/n -> ')
            if user_input == 'y':
                command_elements[0] = temp_command
            else:
                print(INFO_MESSAGE)
                parsed_args = None
                return command_elements[0], parsed_args

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
    elif command_elements[0] == 'birth':
        parsed_args = birth_parser(arguments)
        return command_elements[0], parsed_args
    elif command_elements[0] == 'sort':
        parsed_args = sort_parser(arguments)
        return command_elements[0], parsed_args
    elif command_elements[0] == 'note':
        parsed_args = note_parser(arguments)
        return command_elements[0], parsed_args
    else:
        print(f'Command [{command_elements[0]}] is not found!')

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
    elif command == 'birth':
        serch_contact(arguments.days)
        
def sort_controller(arguments: str):
    run_sorting_files(arguments)

      
def note_controller(arguments: dict):
    if arguments.tag and arguments.replace and arguments.note:
        edit_note(arguments.tag, arguments.replace, arguments.note)
    elif arguments.add and arguments.note:
        print(arguments.add)
        add_note_to_data(arguments.add, arguments.note)
    elif arguments.show == 'all':
        show_all_notes()
    elif arguments.delete:
        delete_note(arguments.delete)
    elif arguments.find:
        find_note(arguments.find)
        
    
  

def main() -> None:
    """
    The main function of the program.
    """
    user_command = ' '.join(argv[1:])
    if not user_command or user_command == '-h':
        print(INFO_MESSAGE)
        return
    
    command, arguments = command_parser(user_command)

    if command in ADDRESSBOOK_COMMANDS and arguments:
        addressbook_controller(command, arguments)
    elif command == 'sort' and arguments:
        sort_controller(arguments.directory)
    elif command == 'note' and arguments:
        note_controller(arguments)
    else:
        print(f'Command *{command}* invalid or used without arguments! Try again or use help.')
        print(INFO_MESSAGE)


if __name__ == '__main__':
    main()