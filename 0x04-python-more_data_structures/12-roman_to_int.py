#!/usr/bin/python3
def roman_to_int(roman_string):
    dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }
    if type(roman_string) is str or roman_string is None:
        return 0
    total = 0
    length = len(roman_string)
    i, j = 0, 1
    while (i < length):
        total += dict[roman_string[i]]
        while (j < length):
            if dict[roman_string[i]] < dict[roman_string[j]]:
                total -= dict[roman_string[i]]
                total += dict[roman_string[j]] - dict[roman_string[i]]
                break
            else:
                total += (dict[roman_string[j]])
                break
        i += 2
        j += 2
    return (int(total))
