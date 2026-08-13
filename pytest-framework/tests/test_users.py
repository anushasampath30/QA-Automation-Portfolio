import pytest
users = [
    ("admin","admin123","Pass"),
    ("anu","welcome","Pass"),
    ("admin","wrong","Fail"),
    ("guest","guest","Fail")
]
@pytest.fixture
def login_init():
    valid_users = {
        "admin": "admin123",
        "anu" : "welcome"
    }
    return valid_users

def login(username,password,login_init):
    
    if login_init.get(username) == password:
        return "Pass"
    return "Fail"
        
    
@pytest.mark.parametrize('username,password,result', users)
def test_login(username,password,result,login_init):
    assert login(username,password,login_init) == result