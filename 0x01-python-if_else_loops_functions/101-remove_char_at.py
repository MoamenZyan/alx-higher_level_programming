#!/usr/bin/python3
def remove_char_at(str, n):
    word = ""
    for i in range(len(str)):
        if (i == n):
            continue
        word += str[i]
    return word
