from abc import ABC, abstractmethod


class Microorganism(ABC):

    @abstractmethod
    def get_genetic_data(self):
        ...


class Virus(Microorganism):
    is_covid: bool

    def get_genetic_data(self):
        pass  # do something


class Bacteria(Microorganism):
    has_kernel: bool

    def get_genetic_data(self):
        pass  # do something

