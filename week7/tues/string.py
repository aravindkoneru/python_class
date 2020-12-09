"""
Goal: Write functions that mimic basic string operations without using any
python string operations.

Basic string operations include:
- combining strings
- checking if something is 'in' a string
- length
- substring using index
- # occurences of a character in a string
- replacing a character in a string with something else

Tip:
- A string can be represented as a list of characters
    - 'abcd' = ['a', 'b', 'c', 'd']
    - 'ab cd' = ['a', 'b', ' ', 'c', 'd']
"""


def combine_strings(first, second):
    """
    combines two strings

    args:
    - first (string)
    - second (string)

    return:
    - a string combining first and second
    """
    # we can't do first+second because that's using a python string function

    # convert first and second to lists
    first = list(first)
    second = list(second)

    # now first and second are lists, so lets combine them
    for char in second:
        first.append(char)

    # converts from list to string
    first = ''.join(first)
    return first


def in_string(base_string, to_check):
    """
    check if to_check is contained within base_string

    args:
    - base_string (string)
    - to_check (a single character)

    return:
    - return True or False depending on whether to_check is in base_string
    """

    # convert base_string to a list
    base_string = list(base_string)

    for char in base_string:
        if char == to_check:
            return True

    # we only get here if we didn't find to_check in base_string
    return False

def length(string):
    """
    return the length of the string without using len()

    args:
    - string (string)

    return:
    - length of string as an integer
    """





result = combine_strings("some string", " other string")
print(result)

result = in_string("some string", "s")
print(result)

