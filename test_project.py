"""
Module to test the project.
"""

import pytest

from exceptions import EmptyListException, WrongListDataTypeException
from project import Comparer


@pytest.fixture
def first_list_larger():
    """
    Method to create a Comparer object where list one average is greater than list two average
    :return: object where list one average is greater than list two average
    """
    return Comparer([2, 3, 4], [1, 2, 3])


@pytest.fixture
def second_list_larger():
    """
    Method to create a Comparer object where list two average is greater than list one average
    :return: object where list two average is greater than list one average
    """
    return Comparer([1, 2, 3], [2, 3, 4])


@pytest.fixture
def even_lists():
    """
    Method to create a Comparer object where both lists average results are even
    :return: object where both lists average results are even
    """
    return Comparer([1, 2, 3], [2, 2, 4, 0])


def test_get_list_one(first_list_larger):
    """
    Method to test
    """
    assert first_list_larger.get_list_one() == [2, 3, 4]


def test_get_list_two(first_list_larger):
    """
    Method to test
    """
    assert first_list_larger.get_list_two() == [1, 2, 3]


def test_list_one_avg_larger(first_list_larger):
    """
    Method to test
    """
    assert first_list_larger.compare() == "Первый список имеет большее среднее значение"


def test_list_two_avg_larger(second_list_larger):
    """
    Method to test
    """
    assert second_list_larger.compare() == "Второй список имеет большее среднее значение"


def test_lists_avg_even(even_lists):
    """
    Method to test
    """
    assert even_lists.compare() == "Средние значения равны"


def test_list_one_empty():
    """
    Method to test
    """
    with pytest.raises(EmptyListException, match="Первый лист пуст"):
        Comparer([], [1, 2, 3])


def test_list_two_empty():
    """
    Method to test
    """
    with pytest.raises(EmptyListException, match="Второй лист пуст"):
        Comparer([1, 2, 3], [])


def test_both_lists_empty():
    """
    Method to test
    """
    with pytest.raises(EmptyListException, match="Оба листа пусты"):
        Comparer([], [])


def test_wrong_data_type():
    """
    Method to test
    """
    with pytest.raises(WrongListDataTypeException, match="Допустимый тип данных в листе: int."
                                                         " Обнаруженный тип данных: str."):
        Comparer([1, 2, 3, "п"], [2, 3, 4])
