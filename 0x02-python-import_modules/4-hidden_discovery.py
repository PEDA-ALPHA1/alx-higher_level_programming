#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import hidden_4
    index = 0
    listt = (dir(hidden_4))
    listlen = len(listt)
    for elements in listt:
        if elements[0] == '_':
            continue
        else:
            print(elements)
