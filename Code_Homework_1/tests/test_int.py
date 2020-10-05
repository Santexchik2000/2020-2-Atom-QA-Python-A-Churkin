import pytest
from random import randint, random


class TestInt:
    value = randint(0, 1000)

    def test_1(self):
        """Тест деления на ноль"""
        with pytest.raises(ZeroDivisionError):
            assert self.value/0

    def test_2(self):
        """Тест метода abs"""
        assert abs(self.value) >= 0

    def test_3(self):
        """Тест функции -х"""
        with pytest.raises(AssertionError):
            assert -self.value > 0

    def test_4(self):
        """Тест оператора равенства"""
        with pytest.raises(AssertionError):
            assert (0.1+0.2) == 0.3

    def test_5(self):
        """Приведение int к str, float, complex """
        assert isinstance(self.value, int)
        assert isinstance(str(self.value), str)
        assert isinstance(float(self.value), float)
        assert isinstance(complex(self.value), complex)
        with pytest.raises(TypeError):
            assert int(complex(1, 4))

    def test_6(self):
        """Приведение str, float, complex к int"""
        assert isinstance(int(float(self.value)), int)
        assert isinstance(complex(str(self.value)), complex)
        assert isinstance(int('111'), int)
        with pytest.raises(ValueError):
            assert int('string')

    @pytest.mark.parametrize('i', range(5))
    def test_7(self, i):
        """Тест проверки целочисленного деления"""
        assert isinstance(self.value // randint(i + 1, 1000), int)

    @pytest.mark.parametrize('a', range(10))
    def test_8(self, a):
        """Тест проверки целочисленного сложения"""
        assert isinstance((self.value+randint(a + 1, 1000)), int)

    @pytest.mark.parametrize('b', range(10))
    def test_9(self, b):
        """Тест проверки сложения комплексных чисел"""
        assert isinstance(
            (complex(self.value+randint(b, 100))+complex(randint(b, 50))), complex)
