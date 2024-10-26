import pytest
from m3 import isPalindrome

def test_isPalindrome():
    assert isPalindrome('madam') == True
    assert isPalindrome('hello') == False

@pytest.mark.parametrize("test_input,expected", [
    ('level', True),
    ('python', False),
    ('racecar', True),
    ('', True),
])
def test_isPalindrome(test_input, expected):
    assert isPalindrome(test_input) == expected
