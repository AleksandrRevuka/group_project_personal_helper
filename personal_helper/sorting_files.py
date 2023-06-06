import os
from os.path import basename
from pathlib import Path
import re


class SortingFiles:
    """Сортування файлів за типами.
    Якщо файл з таким ім'ям вже відсортовано, він пропускається.
    Файли зі старих папок видаляються, порожні папки також видаляються"""

    def __init__(self, path: Path):
        self.path = path
        self.lst_files_addresses: list = []
        self.lst_known: list = []
        self.dict_extensions: dict = {
            "images": [],
            "videos": [],
            "documents": [],
            "audio": [],
            "archives": [],
            "unknown": [],
        }

    def files_addresses(self) -> list:
        """Повертає список всіх файлів та папок зі шляхами"""

        items = self.path.glob(
            "**/*"
        )  # рекурсивно проходить по всіх папках і повертає список шляхів з файлами
        # items має додаткові системні дописи, тому його необхідно перетворити в str
        for item in items:
            if not item.is_dir():  # якщо елемент не є папкою, то:
                self.lst_files_addresses.append(str(item))
        return self.lst_files_addresses

    def sort_extensions(self) -> dict:
        """Повертає словник з груповими списками файлів зі шляхами"""
        for adr in self.lst_files_addresses:
            images_result = re.findall(r"([^/]+[/.](jpeg|png|jpg|svg|bmp))", str(adr))

            if len(images_result) > 0:
                self.dict_extensions["images"].append(adr)
                self.lst_known.append(images_result[0][1])

            videos_result = re.findall(r"([^/]+[/.](avi|mp4|mov|mkv))", str(adr))
            if len(videos_result) > 0:
                self.dict_extensions["videos"].append(adr)
                self.lst_known.append(videos_result[0][1])

            documents_result = re.findall(
                r"([^/]+[/.](docx|doc|txt|pdf|xlsx|pptx))", str(adr)
            )
            if len(documents_result) > 0:
                self.dict_extensions["documents"].append(adr)
                self.lst_known.append(documents_result[0][1])

            audio_result = re.findall(r"([^/]+[/.](mp3|ogg|wav|amr))", str(adr))
            if len(audio_result) > 0:
                self.dict_extensions["audio"].append(adr)
                self.lst_known.append(audio_result[0][1])

            archives_result = re.findall(r"([^/]+[/.](zip|gz|rar|tar))", str(adr))
            if len(archives_result) > 0:
                self.dict_extensions["archives"].append(adr)
                self.lst_known.append(archives_result[0][1])

        list_known_files = []

        for files_list in self.dict_extensions.values():
            for file in files_list:
                list_known_files.append(file)

        lst_unknown = list(
            set(self.lst_files_addresses) - set(list_known_files)
        )  # визначаємо через множини невідомі розширення

        for i in lst_unknown:
            self.dict_extensions["unknown"].append(i)
        return self.dict_extensions

    def removing_files(self) -> None:
        """
        Сортує файли по папках.
        У випадку натрапляння на дублікат файлу, він пропускається
        """

        # 1. Створимо необхідні папки в цільовій папці
        if len(self.dict_extensions["images"]) > 0:
            new_folder = self.path.joinpath("images")
            try:  # Якщо папка вже існує, завдяки try, не буде помилки
                os.mkdir(new_folder)
            except FileExistsError:
                pass

        if len(self.dict_extensions["videos"]) > 0:
            new_folder = self.path.joinpath("videos")
            try:
                os.mkdir(new_folder)
            except FileExistsError:
                pass

        if len(self.dict_extensions["documents"]) > 0:
            new_folder = self.path.joinpath("documents")
            try:
                os.mkdir(new_folder)
            except FileExistsError:
                pass

        if len(self.dict_extensions["audio"]) > 0:
            new_folder = self.path.joinpath("audio")
            try:
                os.mkdir(new_folder)
            except FileExistsError:
                pass

        if len(self.dict_extensions["archives"]) > 0:
            new_folder = self.path.joinpath("archives")
            try:
                os.mkdir(new_folder)
            except FileExistsError:
                pass

        if len(self.dict_extensions["unknown"]) > 0:
            new_folder = self.path.joinpath("unknown")
            try:
                os.mkdir(new_folder)
            except FileExistsError:
                pass

        # 2. Перемістимо файли
        if len(self.dict_extensions["images"]) > 0:
            for way in self.dict_extensions["images"]:
                # Виділимо ім'я файла зі шляху (from os.path import basename)
                file_name = basename(way)  # os.basename
                # Виділимо шлях до файлу
                len_file_name = len(file_name)
                way_without_file_name = way[:-len_file_name]
                new_way = self.path.joinpath("images")
                file_old_place = os.path.join(way_without_file_name, file_name)
                file_new_place = os.path.join(new_way, file_name)
                try:  # Якщо такий файл вже існує, його дублікат не переноситься, а залишається на старому місці
                    # print(way, file_old_place, file_new_place, sep="\n")
                    os.rename(file_old_place, file_new_place)
                except FileExistsError:
                    pass

        if len(self.dict_extensions["videos"]) > 0:
            for way in self.dict_extensions["videos"]:
                # Виділимо ім'я файла зі шляху (from os.path import basename)
                file_name = basename(way)  # os.basename
                # Виділимо шлях до файлу
                len_file_name = len(file_name)
                way_without_file_name = way[:-len_file_name]
                new_way = self.path.joinpath("videos")
                file_old_place = os.path.join(way_without_file_name, file_name)
                file_new_place = os.path.join(new_way, file_name)
                try:  # Якщо такий файл вже існує, його дублікат не переноситься, а залишається на старому місці
                    os.rename(file_old_place, file_new_place)
                except FileExistsError:
                    pass

        if len(self.dict_extensions["documents"]) > 0:
            for way in self.dict_extensions["documents"]:
                # Виділимо ім'я файла зі шляху (from os.path import basename)
                file_name = basename(way)  # os.basename
                # Виділимо шлях до файлу
                len_file_name = len(file_name)
                way_without_file_name = way[:-len_file_name]
                new_way = self.path.joinpath("documents")
                file_old_place = os.path.join(way_without_file_name, file_name)
                file_new_place = os.path.join(new_way, file_name)
                try:  # Якщо такий файл вже існує, його дублікат не переноситься, а залишається на старому місці
                    os.rename(file_old_place, file_new_place)
                except FileExistsError:
                    pass

        if len(self.dict_extensions["audio"]) > 0:
            for way in self.dict_extensions["audio"]:
                # Виділимо ім'я файла зі шляху (from os.path import basename)
                file_name = basename(way)  # os.basename
                # Виділимо шлях до файлу
                len_file_name = len(file_name)
                way_without_file_name = way[:-len_file_name]
                new_way = self.path.joinpath("audio")
                file_old_place = os.path.join(way_without_file_name, file_name)
                file_new_place = os.path.join(new_way, file_name)
                try:  # Якщо такий файл вже існує, його дублікат не переноситься, а залишається на старому місці
                    os.rename(file_old_place, file_new_place)
                except FileExistsError:
                    pass

        if len(self.dict_extensions["archives"]) > 0:
            # print(lst_archives)
            for way in self.dict_extensions["archives"]:
                # Виділимо ім'я файла зі шляху (from os.path import basename)
                file_name = basename(way)  # os.basename
                # Виділимо шлях до файлу
                len_file_name = len(file_name)
                way_without_file_name = way[:-len_file_name]
                new_way = self.path.joinpath("archives")
                file_old_place = os.path.join(way_without_file_name, file_name)
                file_new_place = os.path.join(new_way, file_name)
                try:  # Якщо такий файл вже існує, його дублікат не переноситься, а залишається на старому місці
                    os.rename(file_old_place, file_new_place)
                except FileExistsError:
                    pass

        if len(self.dict_extensions["unknown"]) > 0:
            for way in self.dict_extensions["unknown"]:
                # Виділимо ім'я файла зі шляху (from os.path import basename)
                file_name = basename(way)  # os.basename
                # Виділимо шлях до файлу
                len_file_name = len(file_name)
                way_without_file_name = way[:-len_file_name]
                new_way = self.path.joinpath("unknown")
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
