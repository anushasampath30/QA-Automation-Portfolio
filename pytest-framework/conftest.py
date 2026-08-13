import json
from pathlib import Path

import pytest

from pages.login_service import LoginService
from utils.system_connection import SystemConnection
from utils.database import Database
from data.user_data import USERS


@pytest.fixture(scope="session")
def user_data():
    data_file = Path(__file__).parent / "data" / "users.json"

    with data_file.open("r", encoding="utf-8") as file:
        return json.load(file)


@pytest.fixture
def login_service(user_data):
    return LoginService(user_data["valid_users"])
@pytest.fixture(scope = "module")
def system_connection():
    sysconnect = SystemConnection("25.8.1","ACTIVE")
    sysconnect.connect()
    yield sysconnect
    sysconnect.disconnect()
@pytest.fixture(scope = "module")
def database_connection():
    dataconnect = DatabaseConnection("198.1.1.1")
    dataconnect.connect()
    yield dataconnect
    dataconnect.disconnect()
@pytest.fixture(scope="function")
def database():
    db = Database(":memory:")
    db.connect()
    db.create_users_table()
    for user_id,username,email, status in USERS:
        db.insert_user(user_id,username,email,status)
    yield db
    db.disconnect()





