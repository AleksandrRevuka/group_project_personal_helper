from collections import UserDict
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
        with open('data_notes.json', '+w') as fh:
            json.dump(self.data, fh)

    def load(self):
        """Завантажує нотатки з файлу на диску"""
        with open('data_notes.json', 'r') as fh:
            self.data = json.load(fh)
            return self.data

# Тестування
a = Notes()
# Додавання нотаток з тегами та без тегів (присвоюється порядковий дефолтний "#notag")
a.add_notes('', 'ffff')
a.add_notes('', 'wwwwz')
a.add_notes('', 'wwwwd')
a.add_notes('#aaa', 'aaa')
a.add_notes('#ddd', 'ggggg')
a.add_notes('#bb', 'ccc')
# Додавання нотатки з тегом, який вже є
a.add_notes('#bb', 'ррр')
# Вівід всіх нотаток з тегами
a.show_all_sorted_notes()
# Пошук по нотатках і тегах за існуючим параметром
a.find('g')
# Пошук по нотатках і тегах за неіснуючим параметром
a.find('111111')
# Видалення нотатки за існуючим параметром
a.del_notes('#ddd')
# Видалення нотатки за неіснуючим параметром
a.del_notes('#dd')
# Вівід всіх нотаток з тегами
a.show_all_sorted_notes()
# Редагування нотатки за існуючим параметром
a.edit_notes('#aaa', '#qqq', 'eeeeeeeeeee')
# Редагування нотатки за неіснуючим параметром
a.edit_notes('#d', '#qqq', 'eeeeeeeeeee')
# Вівід всіх нотаток з тегами
a.show_all_sorted_notes()
# Запис даних до файлу
a.save()
# Зчитування даних з файлу
print(a.load())
# Додаткові тести зі зберіганням данних
a.add_notes('#test', 'test')
a.save()
print(a.load())
a.del_notes('#test')
a.save()
print(a.load())

