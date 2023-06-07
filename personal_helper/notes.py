"""..."""
from collections import UserDict
from pathlib import Path
import pickle

try:
    from .constants import FILE_NOTES
except ImportError:
    from constants import FILE_NOTES


class Notes(UserDict):
    """..."""

    def __init__(self) -> None:
        super().__init__()
        self.data: dict = {}

    def add_note(self, tags: list, text: str) -> dict | None:
        """
        The add_note function adds a note to the notes dictionary.
            The function takes two arguments: tags and text. Tags is a list of strings,
            while text is a string. If there are no tags in the list, then it will add
            '#notag' as one of the keys for that note.

        :param self: Represent the instance of the object itself
        :param tags: list: Store the tags that are passed in as a list
        :param text: str: Specify the type of parameter that is expected to be passed in
        """
        tags = tuple(tags)
        if len(tags) == 0:
            tags = ("#notag",)
            if tags not in self.data.keys():
                self.data[tags] = text
                print("Note added!")
                return self.data
            elif tags == ("#notag",) and tags in self.data.keys():
                counter = 1
                while tags in self.data.keys():
                    tags = tuple(["#notag" + str(counter)])
                    counter += 1
                self.data[tags] = text
                print("Note added!")
                return self.data

        for key in self.data.keys():
            for element in key:
                for i in tags:
                    if i == element:
                        print("New tag is already in notes. Note can't be added!")
                        return None
        self.data[tags] = text
        print("Note added!")
        return self.data

    def find(self, key_word: str) -> None:
        """
        The find function searches for a key_word in the data dictionary.
        If it finds the key_word, it prints out all of the tags and text associated with that word.

        :param key_word: str: Search for the key word in the text
        """

        lst = []
        for key, value in self.data.items():
            for element in key:
                if (
                    key_word in element
                    and {key: value} not in lst
                    or key_word in str(value)
                    and {key: value} not in lst
                ):
                    lst.append({key: value})
        if lst:
            print("-" * 50)
            print(f'Search result by parameter "{key_word}":')
            print(("{:^15}|{:^50}".format("TAGS", "TEXT")))
            print("-" * 50)
            for i in lst:
                for key1, value1 in i.items():
                    print("{:<15}|{:<50}".format(", ".join(key1), str(value1)))
            print("-" * 50)
        else:
            print("-" * 50)
            print(f'Nothing was found for parameter "{key_word}".')

    def show_all_sorted_notes(self) -> None:
        """
        The show_all_sorted_notes function prints out all the notes in a sorted order.
        The function takes one argument, self, which is an instance of the FileNotes class.
        The function first prints out a line of dashes to separate it from other functions' output.
        Then it prints &quot;All notes:&quot; and then another line with column headers for tags and text.
        It then creates a list called lst_keys that contains all the keys (tags) in self's data dictionary
        as strings (the keys are tuples).  The list is sorted alphabetically using Python's built-in sort
        method on lists, so that when we iterate through

        :param self: Represent the instance of the class
        """
        print("-" * 50)
        print("All notes:")
        print(("{:^15}|{:^50}".format("TAGS", "TEXT")))
        print("_" * 50)
        lst_keys = list(self.data)
        lst_keys.sort()
        for i in lst_keys:
            print(("{:<15}|{:<50}".format(", ".join(i), self.data[i])))
        print("-" * 50)

    def del_notes(self, tag: str) -> dict:
        """
        The del_notes function deletes a note from the notes dictionary.
            It takes in a tag as an argument and searches for it in the keys of
            the notes dictionary. If it finds one, then it deletes that key-value pair.

        :param self: Represent the instance of the class
        :param tag: str: Specify the tag of the note to be deleted
        """
        copy = self.data.copy()
        flag = True
        while flag:
            for key in copy.keys():
                for element in key:
                    if tag == element:
                        del self.data[key]
                        print('Note with tag "' + tag + '" deleted!')
                        flag = False
            break
        if flag:
            print('Note with tag "' + tag + '" for deleting not found.')
        return self.data

    def edit_notes(self, tag: str, new_tag: list, new_text: str = "") -> dict | None:
        """
        The edit_notes function takes a tag, new_tag and new_text as arguments.
        It searches for the tag in the notes dictionary and if it finds it,
        it deletes that note from the dictionary. Then it adds a new note with
        the given tags and text to the dictionary.

        :param self: Represent the instance of the class
        :param tag: str: Specify the tag of the note to be edited
        :param new_tag: list: Add a new tag to the note
        :param new_text: Change the text of a note
        """
        counter1 = 0
        for key1 in self.data.keys():
            for element1 in key1:
                if element1 == tag:
                    counter1 += 1
                    break
        if counter1 == 0:
            print("No editable tag found!")
            return None

        tags = tuple(new_tag)
        if len(tags) == 0:
            print("No name of new tag!")
            return None

        for key2 in self.data.keys():
            for element2 in key2:
                for i in tags:
                    if i == element2:
                        print("New tag is already in notes. Note can't be added!")
                        return None

        copy = self.data.copy()
        flag = True
        while flag:
            for key3 in copy.keys():
                for element3 in key3:
                    if tag == element3:
                        del self.data[key3]
                        flag = False
            break
        if flag:
            print('Note with tag "' + tag + '" for deleting not found.')
        self.data[tags] = new_text
        return self.data

    def save(self) -> None:
        """
        The save function saves the data in a file.
        """
        with open(FILE_NOTES, "+wb") as fh:
            pickle.dump(self.data, fh)

    def load(self) -> dict:
        """
        The load function is used to load the data from a file.
        If the file does not exist, it will create one and return an empty dictionary.
        """
        if Path(FILE_NOTES).exists():
            with open(FILE_NOTES, "rb") as fh:
                self.data = pickle.load(fh)
                return self.data
        else:
            self.data = {}
            return self.data
