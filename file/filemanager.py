from abc import ABC, abstractmethod


class FileManager(ABC):

    @abstractmethod
    def load(self, path):
        """
        Загружает данные из файла path
        :param path:
        :return:
        """
        pass

    @abstractmethod
    def save(self, path):
        """
        Сохраняет данные по пути path
        :param path:
        :return:
        """
        pass

    @staticmethod
    def isCsv(file):

        if file.split(".").pop() == "csv":
            return True

        return False
