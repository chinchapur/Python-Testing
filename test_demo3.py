#instead of passing to each method we can do using the class
#class name also should start with "Test"
import pytest


@pytest.mark.usefixtures("setup")
class TestFixture_class:

    def test_count1(self):
        print("Execute1")

    def test_count2(self):
        print("Execute2")

    def test_count3(self):
        print("Execute3")

    def test_count4(self):
        print("Execute4")


