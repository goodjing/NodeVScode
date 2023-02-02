import pytest

@pytest.fixture(scope="module")
def open():
    print("打开浏览器，并且打开百度首页")

def test_s1():
    print("用例1：搜索python-1")

def test_s2(open):
    print("用例2：搜索python-2")

def test_s3(open):
    print("用例3：搜索python-3")

if __name__ == "__main__":
    pytest.main(["-s", "test_fixture_module.py"])
