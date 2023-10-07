import pytest
import time

def slow_function():
    time.sleep(5)
    return True

@pytest.mark.slow
def test_something_slow():
    slow_function()
    assert True 
