import pytest


@pytest.mark.usefixtures("getData")
class TestUserData:
    def test_UserData(self,getData):
        print(getData[0])
        print(getData[2])
        print(getData)

#here we r printing the returned data from the fixture and printing it
#So we need to pass the fixture method name as the parameter with the self
#we print using the same name in the method body