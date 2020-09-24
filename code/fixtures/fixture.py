import random
import pytest

@pytest.fixture(scope='class')
def random_func():
    yield random.randint(0,100)
