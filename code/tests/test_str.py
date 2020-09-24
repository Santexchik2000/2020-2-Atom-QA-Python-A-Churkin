import pytest


class TestStr():
    str1="Hello"
    str2="World"

    def test_1(self):
        with pytest.raises(TypeError):
            assert self.str1/self.str2
    
    def test_2(self):
        with pytest.raises(TypeError):
            assert self.str1/int(3)

    def test_3(self):
        """Проверка метода конкатенации str"""
        assert isinstance((self.str1 + ' ' + self.str2),str)
        assert isinstance((self.str1 + str(int(10))),str)
        assert isinstance((self.str1 + str(float(100)) + self.str2), str)

    def test_4(self):
        """Проверяем метод len"""
        assert len(self.str1)==5
        assert len(self.str2+self.str1)==10
        assert len(str(int(10-9)))==1
    
   
    @pytest.mark.parametrize('i',["olleH"])

    def test_5(self,i):
        assert  self.str1==i[::-1]

    @pytest.mark.parametrize('a',["world"])

    def test_6(self,a):
        """проверяем метод title"""
        assert self.str2==a.title()

    @pytest.mark.parametrize('b',["world"])
    
    def test_7(self,b):
        assert b.islower()
        with pytest.raises(AssertionError):
            assert b.isupper()





    

    
    

    

    
  
        
    



        

    
