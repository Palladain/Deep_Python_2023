import pytest
import time

from week06.code.fibonacci import fibonacci_bottom_up, fibonacci_classic


def test_to_check_correctess_fibonacci_classic():
    """
    Напишите тут свои тесты, которые проверяют правильность Фибоначчи
    """
    pass

@pytest.mark.xfail()
def test_to_check_correctess_fibonacci_bottom_up():
    """
    Напишите тут свои тесты, которые проверяют правильность Фибоначчи
    """
    pass


# @pytest.mark.timeout(5)
@pytest.mark.skip()
def test_to_timeout_fibonacci_classic():
    """
    Напишите тут свои тесты, которые проверяют на время Фибоначчи
    Воспользуйтесь @pytest.mark.timeout()
    """
    pass


@pytest.fixture
def timer():
    pass


def test_classic_fibonacci(timer):
    pass