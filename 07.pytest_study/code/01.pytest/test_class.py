# test_class.py
import pytest


class TestClass:
    def test_one(self):
        x = "this"
        assert 't' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'hello')


if __name__ == "__main__":
    pytest.main('-q test_class.py')
