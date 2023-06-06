# group_project_personal_helper
Group project of a personal helper

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