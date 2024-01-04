#!/usr/bin/python3

"""This is my function."""


def text_indentation(text):
    """
    Print two lines after certain characters.

    Parameters:
    - text (str): Text passed to the function.

    Raises:
    - TypeError: If text is not string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(0, len(text)):
        if text[i] in [".", "?", ":"]:
            print(text[i], end="\n")
            print(end="\n")
            continue
        if text[i] == " " and text[i - 1] in [".", "?", ":"]:
            continue
        print(text[i], end="")
