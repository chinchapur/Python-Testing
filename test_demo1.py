#Any pytest file should start with test_ or end with _test
#pytest method names should awlays start with test
#Any code should be wrapped in methods only
#Method name should have sense
# -k stands for method names execution, -s logs in out put -v stands for more info metadata
#you can run specific file name py.test <filename>
#you can mark (tag) tests @pytest.mark.smoke and then run with -m
#you can skip tets with @pytest.mark.skip
#@pytest.mark.xfail is used to xpass the test case and don't show the test results,weather passed or failed
#Fixtures -> @pytest.fixture()
#yield -> (tear down) it will pause this execution & execute remaining methods, atlast it will get executed
#Fixtures are used as setup and tear down methods for test cases
#pip install pytest-html    ->To generate html report
#py.test -v -s --html=report1.html       -->generate an report in html file

import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("Hiii")


@pytest.mark.xfail
def test_secondCreditCard():
    print("Good morning")


def test_thirdCreditCard():
    print("Constructor chaining")


#It will execute first
# @pytest.fixture()
# def setup():
#     print("I will be executed first...")
#     yield
#     print("I will be executed last...")


#We are connecting the non fixture methos with fixture method
#Now this method also comes under fixture
#this will execute after the main fixture method
def test_fixtureDemo(setup):
    print("I will execute steps in fixtureDemo method")

