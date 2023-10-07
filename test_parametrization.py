import pytest

def is_palindrome(s):
    s_without_spaces = s.replace(" ", "")
    return s_without_spaces.lower() == s_without_spaces[::-1].lower()

# def test_is_palindrome_empty_string():
#     assert is_palindrome("")
#
# def test_is_palindrome_single_character():
#     assert is_palindrome("a")
#
# def test_is_palindrome_mixed_casing():
#     assert is_palindrome("Bob")
#
# def test_is_palindrome_with_spaces():
#     assert is_palindrome("Never odd or even")
#
# def test_is_palindrome_with_punctuation():
#     assert is_palindrome("Do geese see God")
#
# def test_is_palindrome_not_palindrome():
#     assert not is_palindrome("abc")
#
# def test_is_palindrome_not_quite():
#     assert not is_palindrome("abab")

@pytest.mark.parametrize("palindrome", [
    "",
    "a",
    "Bob",
    "Never odd or even",
    "Do geese see God",
])
def test_is_palindrome(palindrome):
    assert is_palindrome(palindrome)

@pytest.mark.parametrize("non_palindrome", [
    "abc",
    "abab",
])
def test_is_palindrome_not_palindrome(non_palindrome):
    assert not is_palindrome(non_palindrome)
