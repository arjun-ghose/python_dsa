"""
You have been given a string of lowercase letters.

Write a function called first_non_repeating_char(string) that finds the first non-repeating character in the given
string using a hash table (dictionary). If there is no non-repeating character in the string, the function should return
None.

For example, if the input string is "leetcode", the function should return "l" because "l" is the first character that
appears only once in the string. Similarly, if the input string is "hello", the function should return "h" because "h"
is the first non-repeating character in the string.
"""


def first_non_repeating_char(string: str) -> str | None:
    my_dict = {}
    unique_chars = {}
    non_repeating_chars = {}
    for char in string:
        if char in non_repeating_chars:
            non_repeating_chars.pop(char)
        if char not in unique_chars:
            if char not in my_dict:
                unique_chars[char] = True
                if char not in non_repeating_chars:
                    non_repeating_chars[char] = True
        my_dict[char] = True
    if len(non_repeating_chars) > 0:
        return next(iter(non_repeating_chars))
    else:
        return None



print(first_non_repeating_char('leetcode'))

print(first_non_repeating_char('hello'))

print(first_non_repeating_char('aabbcc'))

"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""
