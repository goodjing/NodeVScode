import pytest

test_user_data = ["admin1", "admin2"]


@pytest.fixture(scope="module")
def login(request):
    user = request.param
    print("登录账户：%s" % user)
    return user


@pytest.mark.parametrize("login", test_user_data, indirect=True)
def test_login(login):
    """登录用例"""
    a = login
    print("测试用例中login的返回值:%s" % a)
    assert a != ""


if __name__ == "__main__":
    pytest.main(["-s", "test02.py"])
