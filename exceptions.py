"""
Module to define exceptions for the project
"""


class MainException(Exception):
    """
    Main exception class
    """
    pass


class EmptyListException(MainException):
    """
    Empty list exception class
    """
    def __init__(self, list_one: list, list_two: list):
        self.list_one = list_one
        self.list_two = list_two

    def __str__(self):
        if not self.list_one and not self.list_two:
            return "Оба листа пусты"
        if not self.list_one:
            return "Первый лист пуст"
        return "Второй лист пуст"


class WrongListDataTypeException(MainException):
    """
    Wrong list data type exception class
    """
    def __init__(self, list_one: list, list_two: list, wrong_type: str):
        self.list_one = list_one
        self.list_two = list_two
        self.wrong_type = wrong_type

    def __str__(self):
        return f"Допустимый тип данных в листе: int. Обнаруженный тип данных: {self.wrong_type}."
