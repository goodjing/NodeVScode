import pytest

def is_true(a):
    if a > 0:
        return True
    else:
        return False

def test_01():
    '''断言xx为真'''
    a = 5
    b = -1
    assert is_true(a), "判断a为真，当前a的值为：%s"%a
    assert not is_true(b), "判断b不为真，当前b的值为：%s"%b

def test_02():
    '''断言b 包含 a'''
    a = "hello"
    b = "hello world"
    assert a in b, "判断b包含a"

def test_03():
    '''断言相等'''
    a = "yoyo"
    b = "yoyo"
    assert a == b, "判断a=b"

def test_04():
    '''断言不等于'''
    a = 5
    b = 6
    assert a != b, "判断a不等于b"

if __name__ == "__main__":
    pytest.main(["-s", "test_assert.py"])