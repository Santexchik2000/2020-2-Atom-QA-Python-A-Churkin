import pytest


class TestStr():
    str1 = "Hello"
    str2 = "World"

    def test_1(self):
        """Тест деления строк"""
        with pytest.raises(TypeError):
            assert self.str1/self.str2

    def test_2(self):
        """Второй Тест деления строк на другой тип"""
        with pytest.raises(TypeError):
            assert self.str1/int(3)

    def test_3(self):
        """Тест проверка метода конкатенации str"""
        assert isinstance((self.str1 + ' ' + self.str2), str)
        assert isinstance((self.str1 + str(int(10))), str)
        assert isinstance((self.str1 + str(float(100)) + self.str2), str)

    def test_4(self):
        """Тест метода len на str"""
        assert len(self.str1) == 5
        assert len(self.str2+self.str1) == 10

    def test_5(self):
        """Тест метода реверсии строки"""
        string1 = "Hello"
        string2 = "olleH"
        assert string1 == string2[::-1]

    @pytest.mark.parametrize('i', range(1, 10))
    def test_6(self, i, random_number):
        assert isinstance((self.str1+str(i)+self.str2+str(random_number)), str)
