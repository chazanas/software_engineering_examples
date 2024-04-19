from enum import Enum


class Kingdom(Enum):
    VIRUS = 0
    BACTERIA = 1
    FUNGI = 2


class Microorganism:
    kingdom: Kingdom
    has_kernel: bool
    is_covid: bool

    def get_genetic_data(self):
        if self.kingdom == Kingdom.VIRUS.value:
            pass # do something
        elif self.kingdom == Kingdom.BACTERIA.value:
            pass # do other thing

