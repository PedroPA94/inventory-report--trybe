from abc import ABC, abstractclassmethod


class Report(ABC):
    @abstractclassmethod
    def generate(cls):
        raise NotImplementedError
