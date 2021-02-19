import pytest


@pytest.fixture(autouse=True, params=['user1', 'user2', 'user3'])
def login(request):
    print("登录方法")
    print(request.param)
    # yield
    yield ['username', 'password']
    print("teardown")
