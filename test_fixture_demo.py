import pytest

# pytest takes a different approach. It leads you toward explicit dependency 
# declarations that are still reusable thanks to the availability of fixtures. 
# pytest fixtures are functions that can create data, test doubles, or initialize 
# system state for the test suite. Any test that wants to use 
# a fixture must explicitly use this fixture function
# as an argument to the test function, so dependencies are always stated up front:

@pytest.fixture
def example_fixture():
    return 1

def test_with_fixture(example_fixture):
    assert example_fixture == 1
