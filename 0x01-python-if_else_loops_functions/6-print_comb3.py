#!/usr/bin/python3
for i in range(0, 100):
    for j in range(i + 1, 100):
        if (j == i % 10 * 10 + int(str(i)[0])):
            if (i < j):
                if (i == 89):
                    print("{:02d}".format(i))
                    break
                print("{:02d}, ".format(i), end="")
                break
