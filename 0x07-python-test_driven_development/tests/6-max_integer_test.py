#!/usr/bin/python3
"""Module for text_indentation method."""


def text_indentation(text):
    """For adding 2 new lines after '.?:' chars.

    Parameters:
        text (str): The first arg.

    Raises:
        TypeError: If text is not a str.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimeter in ".?:":
        # print(delimeter, text.split(delimeter))
        text = (delimeter + "\n\n").join(
            [line.strip(" ") for line in text.split(delimeter)])

    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
