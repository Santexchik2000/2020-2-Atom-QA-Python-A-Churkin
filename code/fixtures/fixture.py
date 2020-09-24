from random import randint, random
import pytest

@pytest.fixture(scope='class')
def random():
    """Возвращает рандомную переменную"""
    yield random.randint(0,100)
