import pytest
from random import randint,random

class Testdict():

    def test_1(self):
        """Тест метода добавления элемента в dict и проверка его наличия в списке"""
        dict1=dict()
        dict1.update({1:'one'})
        assert len(dict1)==1
        assert dict1=={1:'one'}

    def test_2(self):
        """Тест метода создания dict"""
        dict1=dict()
        assert dict1==dict()

    def test_3(self):
        """Тест метода len для dict"""
        dict1=dict()
        assert len(dict1)==0
        dict1.update({1:'one'})
        assert len(dict1)==1
    
    def test_4(self):
        """Тест метода clear для dict и его проверка"""
        dict1=dict()
        dict1.update({1:'one'})
        assert len(dict1)==1
        dict1.clear()
        assert dict1 == dict()

    def test_5(self):
        """Тест метода pop для dict и его проверка"""
        dict1={1:'one',2:'two',3:'three',4:'four',5:'five'}
        assert dict1.get(1)=='one'
        dict1.pop(1)
        with pytest.raises( AssertionError):
            assert len(dict1)==5
    
    @pytest.mark.parametrize('i', range(0,3))
    def test_6(self,i):
        """Тест параметризованного метода на dict, удалением элемента и проверки удаления"""
        dict1={a: a for a in range(0,10)}
        assert dict1.get(i) in dict1
        dict1.pop(i)
        with pytest.raises( AssertionError):
            assert dict1.get(i) in dict1

    @pytest.mark.parametrize('a', range(0,2))
    def test_7(self,a):
        """Тест метода сортировки на dict и его проверка"""
        dict1={4:4,3:3,1:1,2:2,5:5,0:0}
        sorted(dict1)
        assert dict1[a]<dict1[a+1] 