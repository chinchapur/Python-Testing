import pytest
@pytest.mark.usefixtures("getData")
class Test_getData:
    def test_user(self,getData):
        print(getData[0])



def test_fix_parameter(getParam):
    print(getParam[1])