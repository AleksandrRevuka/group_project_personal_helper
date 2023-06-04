from collections import UserDict
from constants import FILE_NOTES
import pickle


class Notes(UserDict):
    """Робота з нотатками"""
    def __init__(self):
        super().__init__()
        self.data = {}

    # Методу потрібен список тегів (можна порожній список)
    def add_notes(self, tags: list, text: str):
        """Додає нотатки з тегами. Якщо тег не задано, то призначається дефолтний тег"""
        tags = tuple(tags)
        if len(tags) == 0:
            tags = ('#notag',)
        if tags not in self.data.keys():
            self.data[tags] = text
        elif tags == ('#notag', ) and tags in self.data.keys():
            counter = 1
            while tags in self.data.keys():
                tags = tuple(['#notag' + str(counter)])
                counter += 1
            self.data[tags] = text
        else:
            print(f"The tag is already exists and can't be added!")
        return self.data

    def find(self, key_word):
        """Пошук за ключовим словом/буквою/символом.
        Пошук ведеться по тегах та по тексту нотатків одночасно."""
        lst = []
        for key, value in self.data.items():
            for element in key:
                if key_word in element and {key: value} not in lst or key_word in str(value) and {key: value} not in lst:
                    lst.append({key: value})
        if lst:
            print('-' * 50)
            print(f'Search result by parameter "{key_word}":')
            print(("{:^15}|{:^50}".format('TAGS', 'TEXT')))
            print('-' * 50)
            for i in lst:
                for key1, value1 in i.items():

                    print("{:<15}|{:<50}".format(', '.join(key1), str(value1)))
            print('-' * 50)
        else:
            print('-' * 50)
            print(f'Nothing was found for parameter "{key_word}".')

    def show_all_sorted_notes(self):
        """Виводить відсортовані за тегами нотатки."""
        """Виводить відсортовані за тегами нотатки."""
        print('-'*50)
        print("All notes:")
        print(("{:^15}|{:^50}".format('TAGS', 'TEXT')))
        print('_'*50)
        # Відсортуємо словник по ключах.
        lst_keys = list(self.data)
        lst_keys.sort()
        for i in lst_keys:
            print(("{:<15}|{:<50}".format(', '.join(i), self.data[i])))
        print('-'*50)

    def del_notes(self, tag: str):
        """Видалення нотатки за тегом"""
        # для запобігання "RuntimeError: dictionary changed size during iteration" ітеруємося по копії
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

    def edit_notes(self, tag: str, new_tag: str, new_text: str):
        """Редагування нотаток"""
        # для запобігання RuntimeError: dictionary changed size during iteration ітеруємося по копії
        copy = self.data.copy()
        flag = True
        while flag:
            for key in copy.keys():
                for element in key:
                    if tag == element:
                        del self.data[key]
                        self.data[(new_tag,)] = new_text
                        print(f'Note with tag "{tag}" has been edited!')
                        flag = False
            break
        if flag:
            print('Note with tag "' + tag + '" for editing not found.')
        return self.data

    def save(self):
        """Зберігає нотатки у файл на диск.
        Якщо файлу не існувало, його буде створено, інакше іде допис у файл"""
        with open(FILE_NOTES, '+wb') as fh:
            pickle.dump(self.data, fh)

    def load(self):
        """Завантажує нотатки з файлу на диску"""
        with open(FILE_NOTES, 'rb') as fh:
            self.data = pickle.load(fh)
            return self.data
