import pytest
from random import randint, random


class Testlist():

    def test_1(self):
        list1=list()
        assert len(list1)==0
        list1.append(1)
        with pytest.raises( AssertionError):
            assert len(list1)==-1
    
    def test_2(self):
        list1=[1,2]
        list2=[3,4]
        assert list1+list2 == [1,2,3,4]

    def test_3(self):
        list1=[1,3]
        list2=[3,1]
        with pytest.raises( AssertionError):
            assert list1==list2
        assert list1[::-1]==list2

    @pytest.mark.parametrize('i', range(1,5))
    def test_4(self,i, random_number):
        list1=list()
        list1.append(random_number)
        assert len(list1)==1
    
    @pytest.mark.parametrize('a', range(1,10))
    def test_5(self,a):
        list1=[randint(0,100) for i in range(1,20)]
        list1.sort()
        assert list1[a]<=list1[a+1]
    



  