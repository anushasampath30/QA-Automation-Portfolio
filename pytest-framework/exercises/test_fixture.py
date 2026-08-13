import pytest

@pytest.fixture(scope="module")
def setup():
    print("Setting up")

    yield

    print("Cleaning up")

def test_one(setup):
    print("Running test1")

def test_two(setup):
    print("Running Test2")