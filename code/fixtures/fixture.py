import random
import pytest


@pytest.fixture(scope='class')
def random_number():
    yield random.randint(0, 100)
