"""
This module implements an address book application with various commands and functionalities.

Available commands:
- add: Create a new contact in the address book. Usage: add -n <name> -p <phone>
- change: Change contact or contact data. Usage: change -n <name> -p <phone> | -e <email> | -b <birthday>
- del: Delete contact or contact data. Usage: del -n <name> -p <phone> | -e <email> | -b <birthday>
- show: Display contact data. Usage: show -a all | show -a <name>
- search: Search contacts by keywords. Usage: search -s <keyword>
- birth: Get contacts with birthdays in the next few days. Usage: birth -d <days>
- sort: Sort files in a directory. Usage: sort -d <directory_path>
- note: Perform operations on notes. 
    Usage: note -a <tag> -n <text_note> | note -f <tag> | note -t <old_tag> -r <new_tag> -n | note -s all | note -d <tag> | note -n <note> | note -r <replace>

For more information about each command, use the -h option after the command name. Example: add -h
"""

import argparse
from sys import argv

try:
    from .constants import ADDRESSBOOK_COMMANDS, LIST_COMMANDS, INFO_MESSAGE
    from .commands import (
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
        birthday_in_next_days,
    )
    from .utils import transformation_commands, get_close_command

except ImportError:
    from constants import ADDRESSBOOK_COMMANDS, LIST_COMMANDS, INFO_MESSAGE
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
        birthday_in_next_days,
    )
    from utils import transformation_commands, get_close_command


def add_parser(arguments: str) -> argparse.Namespace:
    """
    The add_parser function takes a string of arguments and returns an argparse.Namespace object.
    The function uses the argparse module to create a parser for the add command, which is used
    to create new contacts in the phonebook.

    :param arguments: str: Pass the arguments to the function
    """

    usage_info = "\nadd -h\nadd -n <name> -p <phone>"
    parser = argparse.ArgumentParser(
        prog="add", description="Create new contact", usage=usage_info
    )
    parser.add_argument("-n", dest="name", help="Contact name")
    parser.add_argument("-p", dest="phone", help="Number of phone")
    args = parser.parse_args(arguments.split())
    return args


def change_parser(arguments: str) -> argparse.Namespace:
    """
    The change_parser function takes a string of arguments and returns an argparse.Namespace object with the following attributes:
        - name: The contact's name (str)
        - phone: A phone number (str)
        - email: An email address (str)
        - birthday: A date of birth in format dd-mm-yyyy (str)

    :param arguments: str: Pass the command line arguments to the function
    """
    usage_info = "\nchange -h\nchange -n <name> -p <phone> -e\nchange -n <name> -p <phone> -r <phone>\nchange -n <name> -e <email>\nchange -n <name> -e <emeil> -r <emeil>\nchange -n <name> -b <birthday>"
    parser = argparse.ArgumentParser(
        prog="change", description="change contact or contact data", usage=usage_info
    )
    parser.add_argument("-n", dest="name", help="Contact name")
    parser.add_argument("-p", dest="phone", help="Phone Number")
    parser.add_argument("-e", dest="email", help="User Email")
    parser.add_argument(
        "-b", dest="birthday", help="Date of birth in format dd-mm-yyyy"
    )
    parser.add_argument(
        "-r", dest="replace", help="This argument use only after -p or -e"
    )
    args = parser.parse_args(arguments.split())
    return args


def del_parser(arguments: str) -> argparse.Namespace:
    """
    The del_parser function takes a string of arguments and returns an argparse.Namespace object.
    The function is used to parse the command line arguments for the del command.

    :param arguments: str: Pass the command line arguments to the function
    """

    usage_info = "\ndel -h\ndel -n <name>\ndel -n <name> -p <phone>\ndel -n <name> -e <emeil>\ndel-n <name> -b <birthday>"
    parser = argparse.ArgumentParser(
        prog="del", description="delete contact or contact data", usage=usage_info
    )
    parser.add_argument("-n", dest="name", help="Contact name")
    parser.add_argument("-p", dest="phone", help="Phone Number")
    parser.add_argument("-e", dest="email", help="User Email")
    parser.add_argument(
        "-b", dest="birthday", help="Date of birth in format dd-mm-yyyy"
    )
    args = parser.parse_args(arguments.split())
    return args


def show_parser(arguments: str) -> argparse.Namespace:
    """
    The show_parser function takes a string of arguments and returns an argparse.Namespace object.
    The function uses the argparse module to create a parser that can be used to parse the command line arguments for show.
    The parser is created with prog='show', description='display contact data', and usage=usage_info, where usage_info is set to '\nshow -h\nshow -a all\nshow -a &lt;name&gt;'.  The add_argument method adds an argument named &quot;-a&quot; which has dest=&quot;show&quot;, help='Use show -a &lt;all&gt; or show -a &lt;name&gt;'

    :param arguments: str: Pass the arguments that are entered by the user
    """

    usage_info = "\nshow -h\nshow -a all\nshow -a <name>"
    parser = argparse.ArgumentParser(
        prog="show", description="display contact data", usage=usage_info
    )
    parser.add_argument("-a", dest="show", help="Use show -a <all> or show -a <name>")
    args = parser.parse_args(arguments.split())
    return args


def search_parser(arguments: str) -> argparse.Namespace:
    """
    The search_parser function takes in a string of arguments and parses them using the argparse module.
    It returns an object containing the parsed arguments.

    :param arguments: str: Pass the command line arguments to the function
    """

    usage_info = "\nsearch -h\nsearch -s <key_word>"
    parser = argparse.ArgumentParser(
        prog="search", description="search", usage=usage_info
    )
    parser.add_argument("-s", dest="search", help="Search by keywords -s <key word>")
    args = parser.parse_args(arguments.split())
    return args


def birth_parser(arguments: str) -> argparse.Namespace:
    """
    The birth_parser function takes a string of arguments and parses them using the argparse module.
    The function returns an object containing the parsed arguments.

    :param arguments: str: Pass in the command line arguments
    """

    usage_info = "\nbirth -h\nbirth -d <days>"
    parser = argparse.ArgumentParser(
        prog="birth", description="birth", usage=usage_info
    )
    parser.add_argument("-d", dest="days", help="Range of days")
    args = parser.parse_args(arguments.split())
    return args


def sort_parser(arguments: str) -> argparse.Namespace:
    """
    The sort_parser function takes in a string of arguments and returns an argparse.Namespace object.
    The function uses the argparse module to parse the arguments, which are then returned as an object.

    :param arguments: str: Pass in the arguments from the command line
    """

    usage_info = '\nsort -h\nsort -d sort -d <"Path">'
    parser = argparse.ArgumentParser(prog="sort", description="sort", usage=usage_info)
    parser.add_argument("-d", dest="directory", help="Path to directory")
    args = parser.parse_args(arguments.split())
    return args


def note_parser(arguments: str) -> argparse.Namespace:
    """
    The note_parser function takes a string of arguments and parses them into an argparse.Namespace object.
    The function returns the Namespace object, which contains all the parsed arguments as attributes.

    :param arguments: str: Pass in the arguments from the command line
    """

    usage_info = "\nnote -h\note -a <tag> -n <text note>\nnote -f <tag>\nnote -t <old_tag> -r <new_tag> -n\nnote -s all\nnote -d <tag>\nnote -n <note>\nnote -r <replace>"
    parser = argparse.ArgumentParser(prog="note", description="note", usage=usage_info)
    parser.add_argument("-a", dest="add", nargs="+", help="Add new note")
    parser.add_argument("-f", dest="find", help="Find note")
    parser.add_argument("-t", dest="tag", help="Tag")
    parser.add_argument("-s", dest="show", help="Show all note")
    parser.add_argument("-d", dest="delete", help="Delete notes")
    parser.add_argument("-n", dest="note", type=str, nargs="+", help="Note text")
    parser.add_argument("-r", dest="replace", nargs="+", help="New tag")
    args = parser.parse_args(arguments.split())
    if args.note:
        string = ""
        for element in args.note:
            string += element + " "
        args.note = string
    return args


def command_parser(
    user_command: str,
) -> tuple[list[str] | str, argparse.Namespace | None]:
    """
    The command_parser function takes a user command as an argument and returns the parsed arguments.

    :param user_command: str: Store the user input
    """

    command_elements = user_command.split(" ")
    if len(command_elements) < 2:
        arguments = None
        return command_elements[0], arguments

    arguments = user_command.split(" ", 1)[1]
    if command_elements[0] not in LIST_COMMANDS:
        temp_command: str | None = get_close_command(
            transformation_commands(LIST_COMMANDS, command_elements[0])
        )
        if temp_command:
            user_input = input(f"Did you mean command [{temp_command}]? y/n -> ")
            if user_input == "y":
                command_elements[0] = temp_command
            else:
                print(INFO_MESSAGE)
                parsed_args = None
                return command_elements[0], parsed_args

    if command_elements[0] == "add":
        parsed_args = add_parser(arguments)
        return command_elements[0], parsed_args
    elif command_elements[0] == "change":
        parsed_args = change_parser(arguments)
        return command_elements[0], parsed_args
    elif command_elements[0] == "del":
        parsed_args = del_parser(arguments)
        return command_elements[0], parsed_args
    elif command_elements[0] == "show":
        parsed_args = show_parser(arguments)
        return command_elements[0], parsed_args
    elif command_elements[0] == "search":
        parsed_args = search_parser(arguments)
        return command_elements[0], parsed_args
    elif command_elements[0] == "birth":
        parsed_args = birth_parser(arguments)
        return command_elements[0], parsed_args
    elif command_elements[0] == "sort":
        parsed_args = sort_parser(arguments)
        return command_elements[0], parsed_args
    elif command_elements[0] == "note":
        parsed_args = note_parser(arguments)
        return command_elements[0], parsed_args
    else:
        print(f"Command [{command_elements[0]}] is not found!")


def addressbook_controller(command: str | list, arguments: argparse.Namespace) -> None:
    """
    The addressbook_controller function is the main function of this program.
    It takes a command and arguments as input, and then calls the appropriate functions to perform that command.

    :param command: str | list: Determine which command was used
    :param arguments: argparse.Namespace: Get the arguments from the command line
    """

    if command == "add":
        add_contact(arguments.name, arguments.phone)
    elif command == "change":
        if arguments.phone and not arguments.replace:
            add_phone_number_to_contact(arguments.name, arguments.phone)
        elif arguments.phone and arguments.replace:
            change_phone_number_contact(
                arguments.name, arguments.replace, arguments.phone
            )
        elif arguments.email and not arguments.replace:
            add_email_to_contact(arguments.name, arguments.email)
        elif arguments.email and arguments.replace:
            change_email_contact(arguments.name, arguments.replace, arguments.email)
        elif arguments.birthday:
            add_birthday_to_contact(arguments.name, arguments.birthday)
    elif command == "del":
        if arguments.name and arguments.phone:
            delete_phone_number_contact(arguments.name, arguments.phone)
        elif arguments.name and arguments.email:
            delete_email_contact(arguments.name, arguments.email)
        elif arguments.name and not arguments.email and not arguments.phone:
            delete_contact(arguments.name)
    elif command == "show":
        if arguments.show == "all":
            print_contacts()
        elif arguments.show:
            print_contact(arguments.show)
    elif command == "search":
        serch_contact(arguments.search)

    elif command == "birth":
        birthday_in_next_days(arguments.days)


def sort_controller(arguments: str) -> None:
    """
    The sort_controller function is the main function that runs all of the other functions.
    It takes in a string argument, which is what you type into your command line after 'sort_controller.py'.
    The sort_controller function then parses this string and calls other functions to run based on what it finds.

    :param arguments: str: Get the arguments from the command line
    """
    run_sorting_files(arguments)


def note_controller(arguments: argparse.Namespace) -> None:
    """
    The note_controller function is the main function that controls all of the note-related commands.
    It takes in a Namespace object from argparse, which contains all of the arguments passed into it.
    The first if statement checks to see if there are three arguments: tag, replace and note. If so,
    it calls edit_note with those three parameters.

    :param arguments: argparse.Namespace: Pass the arguments from the command line to this function
    """
    if arguments.tag and arguments.replace and arguments.note:
        edit_note(arguments.tag, arguments.replace, arguments.note)
    elif arguments.add and arguments.note:
        print(arguments.add)
        add_note_to_data(arguments.add, arguments.note)
    elif arguments.show == "all":
        show_all_notes()
    elif arguments.delete:
        delete_note(arguments.delete)
    elif arguments.find:
        find_note(arguments.find)


def main() -> None:
    """
    The main function of the program.
    """
    user_command = " ".join(argv[1:])
    if not user_command or user_command == "-h":
        print(INFO_MESSAGE)
        return

    command, arguments = command_parser(user_command)

    if command in ADDRESSBOOK_COMMANDS and arguments:
        addressbook_controller(command, arguments)
    elif command == "sort" and arguments:
        sort_controller(arguments.directory)
    elif command == "note" and arguments:
        note_controller(arguments)
    else:
        print(
            f"Command *{command}* invalid or used without arguments! Try again or use help."
        )
        print(INFO_MESSAGE)


if __name__ == "__main__":
    main()
