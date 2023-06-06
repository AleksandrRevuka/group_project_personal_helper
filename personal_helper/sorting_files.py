"""
This module provides a class, SortingFiles, that can be used to sort files in a directory into different 
categories based on their extensions.

Classes:
- SortingFiles: A class for sorting files into categories and organizing them in subfolders.
"""
import os
from os.path import basename
from pathlib import Path
import re


class SortingFiles:
    """
    SortingFiles class is used to sort files in a directory into different categories and organize them in subfolders.

    Methods:
    - __init__: Initialize the SortingFiles object.
    - files_addresses: Get a list of all file addresses in the specified directory.
    - sort_extensions: Sort the file addresses into different categories based on their extensions.
    - removing_files: Move files from the main folder into subfolders based on their categories.
    - del_empty_folders: Delete empty folders in the directory.

    """

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
        """
        The files_addresses function takes a path object and returns a list of all the files in that directory.
            It does this by using the glob function to find all items in the directory, then appending them to an 
            empty list if they are not directories.
        """

        items = self.path.glob(
            "**/*"
        )
        for item in items:
            if not item.is_dir():
                self.lst_files_addresses.append(str(item))
        return self.lst_files_addresses

    def sort_extensions(self) -> dict:
        """
        The sort_extensions function takes a list of file addresses and sorts them into different categories 
        based on their extensions.The function returns a dictionary with the following keys: 
        images, videos, documents, audio, archives and unknown. 
        Each key has a value that is a list of files with the corresponding extension.
        """

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
        )

        for i in lst_unknown:
            self.dict_extensions["unknown"].append(i)
        return self.dict_extensions

    def removing_files(self) -> None:
        """
        The removing_files function is used to move files from the main folder into subfolders.
        The function creates a new folder for each file type and moves all files of that type into it.

        :param self: Access the attributes and methods of a class
        """

        if len(self.dict_extensions["images"]) > 0:
            new_folder = self.path.joinpath("images")

            try:
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

        if len(self.dict_extensions["images"]) > 0:
            for way in self.dict_extensions["images"]:
                file_name = basename(way)

                len_file_name = len(file_name)
                way_without_file_name = way[:-len_file_name]
                new_way = self.path.joinpath("images")
                file_old_place = os.path.join(way_without_file_name, file_name)
                file_new_place = os.path.join(new_way, file_name)

                try:
                    os.rename(file_old_place, file_new_place)
                except FileExistsError:
                    pass

        if len(self.dict_extensions["videos"]) > 0:
            for way in self.dict_extensions["videos"]:

                file_name = basename(way)

                len_file_name = len(file_name)
                way_without_file_name = way[:-len_file_name]
                new_way = self.path.joinpath("videos")
                file_old_place = os.path.join(way_without_file_name, file_name)
                file_new_place = os.path.join(new_way, file_name)

                try:
                    os.rename(file_old_place, file_new_place)
                except FileExistsError:
                    pass

        if len(self.dict_extensions["documents"]) > 0:
            for way in self.dict_extensions["documents"]:

                file_name = basename(way)

                len_file_name = len(file_name)
                way_without_file_name = way[:-len_file_name]
                new_way = self.path.joinpath("documents")
                file_old_place = os.path.join(way_without_file_name, file_name)
                file_new_place = os.path.join(new_way, file_name)

                try:
                    os.rename(file_old_place, file_new_place)
                except FileExistsError:
                    pass

        if len(self.dict_extensions["audio"]) > 0:
            for way in self.dict_extensions["audio"]:

                file_name = basename(way)

                len_file_name = len(file_name)
                way_without_file_name = way[:-len_file_name]
                new_way = self.path.joinpath("audio")
                file_old_place = os.path.join(way_without_file_name, file_name)
                file_new_place = os.path.join(new_way, file_name)

                try:
                    os.rename(file_old_place, file_new_place)
                except FileExistsError:
                    pass

        if len(self.dict_extensions["archives"]) > 0:

            for way in self.dict_extensions["archives"]:

                file_name = basename(way)

                len_file_name = len(file_name)
                way_without_file_name = way[:-len_file_name]
                new_way = self.path.joinpath("archives")
                file_old_place = os.path.join(way_without_file_name, file_name)
                file_new_place = os.path.join(new_way, file_name)

                try:
                    os.rename(file_old_place, file_new_place)
                except FileExistsError:
                    pass

        if len(self.dict_extensions["unknown"]) > 0:
            for way in self.dict_extensions["unknown"]:

                file_name = basename(way)

                len_file_name = len(file_name)
                way_without_file_name = way[:-len_file_name]
                new_way = self.path.joinpath("unknown")
                file_old_place = os.path.join(way_without_file_name, file_name)
                file_new_place = os.path.join(new_way, file_name)

                try:
                    os.rename(file_old_place, file_new_place)
                except FileExistsError:
                    pass

    def del_empty_folders(self, way: str | None = None) -> None:
        """
        The del_empty_folders function deletes empty folders in the directory.

        :param way: Specify the path of the directory
        """

        for address, dirs, files in os.walk(self.path, topdown=False):
            for d in dirs:
                way = os.path.join(address, d)
                if not os.listdir(way):
                    os.rmdir(way)
