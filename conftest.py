#Instead of creating fixtures in each file, we can write the fixture method in a specific file called as "conftest.py

import pytest

#scope="class" indicates that the fixture scope is class level
#it make it run only once before the class is initialized and once after class executed

@pytest.fixture(scope="class")
def setup():
    print("I will be executed first")
    yield
    print("I will be executed last..")


#In this fixture we r returning the data to the method which it is being called
@pytest.fixture()
def getData():
    print("User profile data is being created..")
    return ["Prakash","Chinchapur","prakashrc3222@gmail.com"]


#Passing parameter to the fixture and request is the parameter to the method
#using request.param we can return the values from the list one by one
#If you want to multiple values at a time then specify value inside ()
@pytest.fixture(params=[("chrome","Prakash","Chinchapur"),("Firefox","Ganesh","Kodmur"),"IE"])
def crossBrowser(request):
    return  request.param



