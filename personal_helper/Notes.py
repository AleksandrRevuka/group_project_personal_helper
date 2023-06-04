from collections import UserDict
from constants import FILE_NOTES
import json


class Notes(UserDict):
    """Робота з нотатками"""
    def __init__(self):
        super().__init__()
        self.data = {}

    def add_notes(self, tag, text):
        """Додає нотатки з тегами. Якщо тег не задано, то призначається дефолтний тег"""
        if tag == '':
            tag = '#notag'
        if tag not in self.data.keys():
            self.data[tag] = text
        elif tag == '#notag' and tag in self.data.keys():
            counter = 1
            while tag in self.data.keys():
                tag = '#notag' + str(counter)
                counter += 1
            self.data[tag] = text
        else:
            print(f"The tag '{tag}' is already exists and can't be added!")
        return self.data

    def find(self, key_word):
        """Пошук за ключовим словом/буквою/символом.
        Пошук ведеться по тегах та по тексту нотатків одночасно."""
        lst = []
        for key, value in self.data.items():
            if key_word in str(key) and {key: value} not in lst or key_word in str(value) and {key: value} not in lst:
                lst.append({key: value})
        if lst:
            print('-' * 50)
            print(f'Search result by parameter "{key_word}":')
            print(("{:^15}|{:^50}".format('TAGS', 'TEXT')))
            print('-' * 50)
            for i in lst:
                for key1, value1 in i.items():
                    print("{:<15}|{:<50}".format(key1, str(value1)))
            print('-' * 50)
        else:
            print('-' * 50)
            print(f'Nothing was found for parameter "{key_word}".')
            print('-' * 50)

    def show_all_sorted_notes(self):
        """Виводить відсортовані за тегами нотатки."""
        print('-'*50)
        print("All notes:")
        print(("{:^15}|{:^50}".format('TAGS', 'TEXT')))
        print('_'*50)
        # Відсортуємо словник по ключах.
        lst_keys = list(self.data)
        lst_keys.sort()
        for i in lst_keys:
            print(("{:<15}|{:<50}".format(i, self.data[i])))
        print('-'*50)

    def del_notes(self, tag: str):
        """Для видалення необхідно вказати всі теги нотатки, як показує show_all_sorted_notes"""
        if tag in self.data.keys():
            del self.data[tag]
            print('Note with tag "' + tag + '" deleted!')
        else:
            print('Note with tag "' + tag + '" for deleting not found.')
        return self.data

    def edit_notes(self, tag: str, new_tag: str, new_text: str):
        """Редагування нотаток"""
        if tag in self.data.keys():
            del self.data[tag]
            self.data[new_tag] = new_text
            print(f'Note for tag "{tag}" has been edited!')
            return self.data
        else:
            print("Note with tag " + tag + " for editing not found.")

    def save(self):
        """Зберігає нотатки у файл на диск.
        Якщо файлу не існувало, його буде створено, інакше іде допис у файл"""
        with open(FILE_NOTES, '+w') as fh:
            json.dump(self.data, fh)

    def load(self):
        """Завантажує нотатки з файлу на диску"""
        with open(FILE_NOTES, 'r') as fh:
            self.data = json.load(fh)
            return self.data

