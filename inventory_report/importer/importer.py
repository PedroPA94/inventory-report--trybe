from abc import ABC, abstractclassmethod


class Importer(ABC):
    @abstractclassmethod
    def import_data(cls, path_to_file: str):
        raise NotImplementedError
