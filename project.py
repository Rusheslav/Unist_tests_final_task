"""
This module defines the Comparer class to compare the average of two lists.
"""
from exceptions import EmptyListException, WrongListDataTypeException


class Comparer:
    """
    Class to compare the average of two lists of integers.
    """
    def __init__(self, list_one: list[int], list_two: list[int]):
        if list_one == [] or list_two == []:
            raise EmptyListException(list_one, list_two)
        for checked_list in [list_one, list_two]:
            for element in checked_list:
                if not isinstance(element, int):
                    raise WrongListDataTypeException(list_one, list_two, type(element).__name__)
        self.list_one = list_one
        self.list_two = list_two
        self.list_one_avg = sum(list_one) / len(list_one)
        self.list_two_avg = sum(list_two) / len(list_two)

    def compare(self):
        """
        Method to compare the average of the two object lists.
        :return: the result of the comparison.
        """
        if self.list_one_avg > self.list_two_avg:
            return "Первый список имеет большее среднее значение"
        if self.list_one_avg < self.list_two_avg:
            return "Второй список имеет большее среднее значение"
        if self.list_one_avg == self.list_two_avg:
            return "Средние значения равны"
        return "Неожиданная ошибка"

    def get_list_one(self):
        """
        Method returning list one
        :return:list one
        """
        return self.list_one

    def get_list_two(self):
        """
        Method returning list two
        :return:list two
        """
        return self.list_two
