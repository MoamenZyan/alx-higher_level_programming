#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    if (len(argv) - 1 == 0):
        print("{} {}.".format(len(argv) - 1, "arguments"))
    else:
        print("{} {}:".format(len(argv) - 1, "arguments"))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
