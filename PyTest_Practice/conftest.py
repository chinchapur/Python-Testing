import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will execute first as i'm an fixture...")
    yield
    print("I will execute at the last, as i'm written in yield")


@pytest.fixture()
def getData():
    return ["Prakash","Chinchapur","prakashrc3222@gmail.com"]


@pytest.fixture(params=[("Chrome","Ram"),("Firefox","Ganesh"),("Edge","Gunderao")])
def getParam(request):
    return request.param