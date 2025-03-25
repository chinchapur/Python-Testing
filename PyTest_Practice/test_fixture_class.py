import pytest


@pytest.mark.usefixtures("setup")
class Test_fixture:
    def test_fixyure_demo1(self):
        print("Method of fixture demo1")

    def test_fixyure_demo2(self):
        print("Method of fixture demo2")

    def test_fixyure_demo3(self):
        print("Method of fixture demo3")

    def test_fixyure_demo4(self):
        print("Method of fixture demo4")