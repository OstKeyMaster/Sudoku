"""
Класс "Клеточка"

Собственность @vlad.ostas :-)
"""


class Cell:
    def __init__(self, value, chunk):
        self.__digit = value
        if self.__digit == 0:
            self.__possible_answers = list(range(1, 10))
        else:
            self.__possible_answers = []
        self.__chunk = chunk

    @property
    def digit(self):
        return self.__digit

    @digit.setter
    def digit(self, value):  # TODO
        self.__digit = value

    def possibles(self):
        return self.__possible_answers

    def remove_possible(self, value):
        try:
            self.__possible_answers.remove(value)
            return True
        except ValueError:
            return False

    def __str__(self):
        return f'{self.__digit} | {self.__possible_answers}'
