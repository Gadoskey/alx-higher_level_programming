#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    previous_value = 0
    for character in reversed(roman_string):
        current_value = roman_dict[character]
        if current_value >= previous_value:
            total = total + current_value
        else:
            total = total - current_value

        previous_value = current_value

    return total
