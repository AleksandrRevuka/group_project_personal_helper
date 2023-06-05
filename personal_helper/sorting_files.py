import os
from os.path import basename
from pathlib import Path
import re


# перед створенням цього класу треба прописати перевірку, що шлях існує і вказує на папку
#     if path.exists():
#     else:
#         print(f'The way is not exists!')

class SortingFiles:
    """Сортування файлів за типами.
     Якщо файл з таким ім'ям вже відсортовано, він пропускається.
     Файли зі старих папок видаляються, порожні папки також видаляються"""
    def __init__(self, path: Path):
        self.path = path
        self.lst_files_addresses: list = []
        self.lst_known: list = []
        self.dict_extensions: dict = {
            'images': [],
            'videos': [],
            'documents': [],
            'audio': [],
            'archives': [],
            'unknown': []
        }

    def files_addresses(self) -> list:
        """Повертає список всіх файлів та папок зі шляхами"""

        items = self.path.glob('**/*')  # рекурсивно проходить по всіх папках і повертає список шляхів з файлами
        # items має додаткові системні дописи, тому його необхідно перетворити в str
        for item in items:
            if not item.is_dir():  # якщо елемент не є папкою, то:
                self.lst_files_addresses.append(str(item))
        return self.lst_files_addresses

    def sort_extensions(self) -> dict:
        """Повертає словник з груповими списками файлів зі шляхами"""

        for i in self.lst_files_addresses:

            images_result = re.findall(r"([^/]+[/.](jpeg|png|jpg|svg|bmp))", str(i))
            if len(images_result) > 0:
                for i in images_result:
                    self.dict_extensions['images'].append(i[0])
                    self.lst_known.append(i[0])

            videos_result = re.findall(r"([^/]+[/.](avi|mp4|mov|mkv))", str(i))
            if len(videos_result) > 0:
                for i in videos_result:
                    self.dict_extensions['videos'].append(i[0])
                    self.lst_known.append(i[0])

            documents_result = re.findall(r"([^/]+[/.](docx|doc|txt|pdf|xlsx|pptx))", str(i))
            if len(documents_result) > 0:
                for i in documents_result:
                    self.dict_extensions['documents'].append(i[0])
                    self.lst_known.append(i[0])

            audio_result = re.findall(r"([^/]+[/.](mp3|ogg|wav|amr))", str(i))
            if len(audio_result) > 0:
                for i in audio_result:
                    self.dict_extensions['audio'].append(i[0])
                    self.lst_known.append(i[0])

            archives_result = re.findall(r"([^/]+[/.](zip|gz|rar|tar))", str(i))
            if len(archives_result) > 0:
                for i in archives_result:
                    self.dict_extensions['archives'].append(i[0])
                    self.lst_known.append(i[0])

        lst_unknown = list(set(self.lst_files_addresses) - set(self.lst_known))  # визначаємо через множини невідомі розширення
        for i in lst_unknown:
            self.dict_extensions['unknown'].append(i)
        return self.dict_extensions

    def removing_files(self) -> None:
        """
        Сортує файли по папках.
        У випадку натрапляння на дублікат файлу, він пропускається
        """

        # 1. Створимо необхідні папки в цільовій папці
        if len(self.dict_extensions['images']) > 0:
            new_folder = str(self.path) + '\\images'
            try:  # Якщо папка вже існує, завдяки try, не буде помилки
                os.mkdir(new_folder)
            except FileExistsError:
                pass

        if len(self.dict_extensions['videos']) > 0:
            new_folder = str(self.path) + '\\videos'
            try:
                os.mkdir(new_folder)
            except FileExistsError:
                pass

        if len(self.dict_extensions['documents']) > 0:
            new_folder = str(self.path) + '\\documents'
            try:
                os.mkdir(new_folder)
            except FileExistsError:
                pass

        if len(self.dict_extensions['audio']) > 0:
            new_folder = str(self.path) + '\\audio'
            try:
                os.mkdir(new_folder)
            except FileExistsError:
                pass

        if len(self.dict_extensions['archives']) > 0:
            new_folder = str(self.path) + '\\archives'
            try:
                os.mkdir(new_folder)
            except FileExistsError:
                pass

        if len(self.dict_extensions['unknown']) > 0:
            new_folder = str(self.path) + '\\unknown'
            try:
                os.mkdir(new_folder)
            except FileExistsError:
                pass

        # 2. Перемістимо файли
        if len(self.dict_extensions['images']) > 0:
            for way in self.dict_extensions['images']:
                # Виділимо ім'я файла зі шляху (from os.path import basename)
                file_name = basename(way)  # os.basename
                # Виділимо шлях до файлу
                len_file_name = len(file_name)
                way_without_file_name = way[:-len_file_name]
                new_way = str(self.path) + '\\images'
                file_old_place = os.path.join(way_without_file_name, file_name)
                file_new_place = os.path.join(new_way, file_name)
                try:  # Якщо такий файл вже існує, його дублікат не переноситься, а залишається на старому місці
                    os.rename(file_old_place, file_new_place)
                except FileExistsError:
                    pass

        if len(self.dict_extensions['videos']) > 0:
            for way in self.dict_extensions['videos']:
                # Виділимо ім'я файла зі шляху (from os.path import basename)
                file_name = basename(way)  # os.basename
                # Виділимо шлях до файлу
                len_file_name = len(file_name)
                way_without_file_name = way[:-len_file_name]
                new_way = str(self.path) + '\\videos'
                file_old_place = os.path.join(way_without_file_name, file_name)
                file_new_place = os.path.join(new_way, file_name)
                try:  # Якщо такий файл вже існує, його дублікат не переноситься, а залишається на старому місці
                    os.rename(file_old_place, file_new_place)
                except FileExistsError:
                    pass

        if len(self.dict_extensions['documents']) > 0:
            for way in self.dict_extensions['documents']:
                # Виділимо ім'я файла зі шляху (from os.path import basename)
                file_name = basename(way)  # os.basename
                # Виділимо шлях до файлу
                len_file_name = len(file_name)
                way_without_file_name = way[:-len_file_name]
                new_way = str(self.path) + '\\documents'
                file_old_place = os.path.join(way_without_file_name, file_name)
                file_new_place = os.path.join(new_way, file_name)
                try:  # Якщо такий файл вже існує, його дублікат не переноситься, а залишається на старому місці
                    os.rename(file_old_place, file_new_place)
                except FileExistsError:
                    pass

        if len(self.dict_extensions['audio']) > 0:
            for way in self.dict_extensions['audio']:
                # Виділимо ім'я файла зі шляху (from os.path import basename)
                file_name = basename(way)  # os.basename
                # Виділимо шлях до файлу
                len_file_name = len(file_name)
                way_without_file_name = way[:-len_file_name]
                new_way = str(self.path) + '\\audio'
                file_old_place = os.path.join(way_without_file_name, file_name)
                file_new_place = os.path.join(new_way, file_name)
                try:  # Якщо такий файл вже існує, його дублікат не переноситься, а залишається на старому місці
                    os.rename(file_old_place, file_new_place)
                except FileExistsError:
                    pass

        if len(self.dict_extensions['archives']) > 0:
            # print(lst_archives)
            for way in self.dict_extensions['archives']:
                # Виділимо ім'я файла зі шляху (from os.path import basename)
                file_name = basename(way)  # os.basename
                # Виділимо шлях до файлу
                len_file_name = len(file_name)
                way_without_file_name = way[:-len_file_name]
                new_way = str(self.path) + '\\archives'
                file_old_place = os.path.join(way_without_file_name, file_name)
                file_new_place = os.path.join(new_way, file_name)
                try:  # Якщо такий файл вже існує, його дублікат не переноситься, а залишається на старому місці
                    os.rename(file_old_place, file_new_place)
                except FileExistsError:
                    pass

        if len(self.dict_extensions['unknown']) > 0:
            for way in self.dict_extensions['unknown']:
                # Виділимо ім'я файла зі шляху (from os.path import basename)
                file_name = basename(way)  # os.basename
                # Виділимо шлях до файлу
                len_file_name = len(file_name)
                way_without_file_name = way[:-len_file_name]
                new_way = str(self.path) + '\\unknown'
                file_old_place = os.path.join(way_without_file_name, file_name)
                file_new_place = os.path.join(new_way, file_name)
                try:  # Якщо такий файл вже існує, його дублікат не переноситься, а залишається на старому місці
                    os.rename(file_old_place, file_new_place)
                except FileExistsError:
                    pass

    def del_empty_folders(self, way=None) -> None:
        """Видаляє порожні теки на всіх рівнях вкладення"""
        for address, dirs, files in os.walk(self.path):
            for d in dirs:  # Для всіх папок (і вкладених також) в self.path
                way = os.path.join(address, d)  # Створює шляхи до всіх папок
                if not os.listdir(way):  # Якщо папка порожня
                    os.rmdir(way)  # Видалення порожньої папки

