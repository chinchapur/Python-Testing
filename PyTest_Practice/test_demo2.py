import pytest


# @pytest.mark.skip
@pytest.mark.xfail
def test_CreditCard(setup):
    msg = "Hello"
    test_debitCard()
    assert msg == "Hii","Failed bcz string doesn't match"


@pytest.mark.smoke
def test_debitCard(setup):
    a = 6
    b= 5
    assert a-1 == b