import pytest
from random import randint, random


class Testlist():

    def test_1(self):
        """Тест метода создания list"""
        list1 = list()
        assert isinstance(list1, list)

    def test_2(self):
        """Тест метода len на пустом list"""
        list1 = list()
        assert len(list1) == 0

    def test_3(self):
        """Тест операции конкатенации на list"""
        list1 = [1, 2]
        list2 = [3, 4]
        assert list1+list2 == [1, 2, 3, 4]

    def test_4(self):
        """Тест метода реверсии списков и проверка его на list"""
        list1 = [1, 3]
        list2 = [3, 1]
        assert list1[::-1] == list2

    def test_5(self, random_number):
        """Тест проверки работы метода append на list"""
        list1 = list()
        list1.append(random_number)
        assert list1 == [random_number]

    @pytest.mark.parametrize('a', range(1, 10))
    def test_6(self, a):
        """Тест метода сортировки на list и его проверка"""
        list1 = [randint(0, 100) for i in range(1, 20)]
        list1.sort()
        assert list1[a] <= list1[a+1]
