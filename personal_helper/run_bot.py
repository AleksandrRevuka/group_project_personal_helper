import argparse
from sys import argv
import os.path

from address_book import AddressBook
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


def build_parser(arguments: str):
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


def command_parser(user_command: str):
    command_elements = user_command.split(' ')
    if len(command_elements) < 2:
        arguments = None
        return command_elements[0], arguments
    else:
        arguments = user_command.split(' ', 1)[1]
        parsed_args = build_parser(arguments)
        return command_elements[0], parsed_args
    

def load_contact_book():
    contact_book = AddressBook()
    if os.path.exists('Address_Book.bin'):
        contact_book.read_records_from_file('address_book.bin')
    return contact_book
    

def main():
    contact_book = load_contact_book()
    # Забираєм аліас самого бота
    user_command = ' '.join(argv[1:])
    command, arguments = command_parser(user_command)
    if not arguments:
        
        print('Команди без аргументів або помилка')
    else:
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
                
                
        print('Ми маємо аргументи')
        print(arguments)


if __name__ == '__main__':
    main()
    
