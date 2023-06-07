"""
The constants module provides constant values used in the address book application.

This module defines various constant values used in the application, such as file paths,
number of contacts per page, and ranges for name and phone number lengths.
"""

import os
from string import ascii_letters
from pathlib import Path

current_dir = str(Path.home())
FILE = os.path.join(current_dir, "address_book.bin")
FILE_NOTES = os.path.join(current_dir, "data_notes.bin")

NUMBER_OF_CONTACTS_PER_PAGE = 20

CYRILLIC = "абвгґдеєёжзиіїйклмнопрстуфхцчшщъыьэюя. ʼ"
LETTERS = ascii_letters + CYRILLIC + CYRILLIC.upper()
NAME_RANGE = range(1, 50)
PHONE_RANGE = range(7, 20)

ADDRESSBOOK_COMMANDS = ["add", "change", "del", "show", "search", "birth"]
LIST_COMMANDS = ["add", "change", "del", "show", "search", "birth", "note", "sort"]

INFO_MESSAGE = "Use command:\nadd\nchange\ndel\nshow\nsearch\nbirth\nnote\nsort\n\nDetail about command:\n[command] -h"
