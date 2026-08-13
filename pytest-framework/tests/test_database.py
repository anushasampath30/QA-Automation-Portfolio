import pytest
import sqlite3
from data.user_data import USERS
ip_details =[
    ("192.168.1.1",True),
    ("10.0.0.1",True),
    ("256.1.1.1",False),
    ("192.168.1",False),
    ("abc.def.1.1",False),
    ("",False)
]
def validate_ip(ip):
    parts = ip.split(".")
    if len(parts)==4 and ip.replace(".","").isdigit():
        if all(0 <= int(p) <= 255 for p in parts):
            return True
        else:
            return False
    else:
        return False


    
@pytest.mark.parametrize('ip,result', ip_details)
def test_database(ip,result):
    assert validate_ip(ip)==result
@pytest.mark.parametrize("user_id,username,email,status",USERS)
def test_users_exists(database,user_id,username,email,status):
    user = database.get_user(username)
    assert user is not None
    assert user[0] == user_id
    assert user[1] == username
    assert user[2] == email
    assert user[3] == status

status_counts = [
    ("ACTIVE",2),
    ("INACTIVE",1)
]
@pytest.mark.parametrize('status,expected_count',status_counts)
def test_users_by_status(database,status,expected_count):
    status_users = database.get_user_status(status)
    assert len(status_users) == expected_count
update_cases = [
    ("guest", "INACTIVE", "ACTIVE"),
    ("admin", "ACTIVE", "INACTIVE"),
    ("anu", "ACTIVE", "INACTIVE"),
]
@pytest.mark.parametrize('username,old_status,new_status',update_cases)
def test_update_user_status(database,username,old_status,new_status):
    user_before = database.get_user(username)
    assert user_before is not None
    assert user_before[3] == old_status
    database.update_user_status(username,new_status)
    user_after = database.get_user(username) 
    assert user_after[3] == new_status

def test_duplicate_user_id(database):
    
    with pytest.raises(sqlite3.IntegrityError) as error:
        database.insert_user(1,"newuser","newuser@test.com","INACTIVE")
    assert "UNIQUE constraint failed" in str(error.value)    