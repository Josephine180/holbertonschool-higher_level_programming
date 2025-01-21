#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for char in roman_string:
        number = roman_dict.get(char)
        if number is None:
            return 0

        if number > prev_value:
            total += number - 2 * prev_value
        else:
            total += number
        prev_value = number

    return total
