"""
Write a function called has_unique_chars that takes a string as input and returns True if all the characters in the
string are unique, and False otherwise.

For example, has_unique_chars('abcdefg') should return True, while has_unique_chars('hello') should return False.
"""

def has_unique_chars(string: str) -> bool:
    unique_chars = set()
    for i, char in enumerate(string):
        unique_chars.add(char)
    if len(unique_chars) < len(string):
        return False
    return True


print(has_unique_chars('abcdefg'))  # should return True
print(has_unique_chars('hello'))  # should return False
print(has_unique_chars(''))  # should return True
print(has_unique_chars('0123456789'))  # should return True
print(has_unique_chars('abacadaeaf'))  # should return False

"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    True
    True
    False

"""
