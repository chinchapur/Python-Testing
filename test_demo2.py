import pytest


@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hii", "Test failed bcz strings donot match"

#here we r passing fixture as a parameter but we can reduce it instead of passing to each methods
def test_demos(setup):
    print("Extending the fixture setup")


@pytest.mark.smoke
def test_secondCreditCard(setup):
    a = 4
    b= 6
    assert a+2 == 6, "Addition deosn't match"

