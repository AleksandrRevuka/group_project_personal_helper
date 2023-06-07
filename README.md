# Personal Helper

Personal Helper is a Python module that provides classes and functions for managing an address book, contact records, and performing various operations. It allows users to create, edit, and delete contacts, add phone numbers and emails, search for contacts, sort files in a directory, and perform operations on notes.

## Available commands

- **add**: Create a new contact in the address book.
    - Usage: `add -n <name> -p <phone>`
    - Example: `add -n John`
    - Example: `add -n John -p 1234567890`

- **change**: Change contact or contact data.
    - Usage: `change -n <name> -p <phone> | -e <email> | -b <birthday>`
    - Example: `change -n John -p 1234567890 -r 0987654321`
    - Example: `change -n John -e johndoe@example.com -r j_doe@example.com`
    - Example: `change -n John -b 29-02-2020`

- **del**: Delete contact or contact data.
    - Usage: `del -n <name> -p <phone> | -e <email>`
    - Example: `del -n John`
    - Example: `del -n John -e johndoe@example.com`
    - Example: `del -n John -p 1234567890`

- **show**: Display contact data.
    - Usage: `show -a all | show -a <name>`
    - Example: `show -a all`
    - Example: `show -a John`

- **search**: Search contacts by keywords.
    - Usage: `search -s <keyword>`
    - Example: `search -s John`
    - Example: `search -s 1234`

- **birth**: Get contacts with birthdays in the next few days.
    - Usage: `birth -d <days>`
    - Example: `birth -d 7`

- **sort**: Sort files in a directory.
    - Usage: `sort -d <directory_path>`
    - Example: `sort -d /path/to/directory`

- **note**: Perform operations on notes.
    - Usage: `note -a <tag> -n <text_note> | note -f <tag> | note -t <old_tag> -r <new_tag> -n <text_note> | note -s all | note -d <tag>`
    - Example: `note -a work -n "Remember to submit the report"`
    - Example: `note -a work job -n "Remember to submit the report"`
    - Example: `note -f work`
    - Example: `note -t work -r job -n "Remember to submit the report"`
    - Example: `note -s all`
    - Example: `note -d work`


For more information about each command, use the `-h` option after the command name. Example: `add -h`

## Installation

To use Personal Helper, you need to have Python installed on your system. You can install the module using pip:

pip install personal_helper


## Usage

Here is an example of how to use Personal Helper to create and manage an address book and perform various operations:

```python
from personal_helper.address_book import AddressBook, Record
from personal_helper.entities import User, Phone, Email

# Create an address book
address_book = AddressBook()

# Create a contact record
user = User("John")
record = Record(user)

# Add phone number and email to the contact record
phone_number = Phone("1234567890")
email = Email("johndoe@example.com")
record.add_phone_number(phone_number)
record.add_email(email)

# Add the contact record to the address book
address_book.add_record(record)

# Print all contacts in the address book
address_book.print_contacts()

# Search for contacts matching a criteria
search_results = address_book.search("John")
print(search_results)

# Delete a contact record from the address book
address_book.delete_record("John")
```

## Documentation
The documentation for Personal Helper can be found in the Personal Helper Documentation.

## Contributing
Contributions to Personal Helper are welcome! If you find any issues or have suggestions for improvements, please create a GitHub issue or submit a pull request.

## License
Personal Helper is licensed under the MIT License.

 ## Credits
Personal Helper was developed by ['Oleksandr Revuka', 'Oleksandr Shevchenko', 'Evgen Kulik', 'Roman Lomachinskiy', 'Oleksii Chaika', 'Artem Ivanina'].
