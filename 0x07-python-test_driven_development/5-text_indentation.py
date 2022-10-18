#!/usr/bin/python3
"""
prints text with 2 new lines after each ".", "?", and ":"
Takes in a string
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each ".", "?", and ":"
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    list_of_lines = [lines.strip(' ') for lines in text.split('\n')]
    indented = "\n".join(list_of_lines)
    print(indented, end="")

