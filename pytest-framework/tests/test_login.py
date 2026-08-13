import pytest
@pytest.mark.smoke
def test_valid_admin_login(login_service):
    assert login_service.login("admin", "admin123")
users =  [
        ("admin", "admin123", True),
        ("anu", "welcome", True),
        ("admin", "wrong", False),
        ("guest", "guest", False),
        ("", "", False),
    ]
@pytest.mark.regression
@pytest.mark.parametrize("username,password,expected", users)
def test_login_cases(login_service,username,password,expected):
    actual_result = login_service.login(username,password)
    assert actual_result == expected