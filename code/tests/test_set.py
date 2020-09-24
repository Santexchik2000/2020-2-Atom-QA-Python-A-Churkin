import pytest
from random import randint, random

class Testset():


    def test_1(self):
        set1={'1','2'}
        set2={'3','4'}
        assert set1.union(set2)=={'1','2','3','4'}

    def test_2(self):
        a=randint(10, 1000)  
        set1=set() 
        assert len(set1)==0
        assert set1.add(a) is None
        assert len(set1)==1
    
    def test_3(self):
        set1={'1','2','3','4'}
        set1.remove('1')
        assert len(set1)==3
        assert set1=={'2','3','4'}

    def test_4(self):
        set1={1,3,2}
        assert sum(set1)== 6
        set1.add(4)
        assert sum(set1)==10
    
    def test_5(self):
        """тест метода clear"""
        set1=set()
        set1.add(1)
        assert len(set1)==1
        assert set1.clear() is None
        assert len(set1) == 0

    @pytest.mark.parametrize('i',range(1,9))

    def test_6(self,i):
        set1=set()
        set1.add(i)
        assert i in set1
    
   
      
        



    
