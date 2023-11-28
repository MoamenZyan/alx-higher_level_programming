#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if (i % 3 == 0):
            x = "Fizz"
        elif (i % 5 == 0):
            x = "Buzz"
        elif (i % 5 == 0 and i % 3 == 0):
            x = "FizzBuzz"
        else:
            x = i

        if (i == 100):
            print("{}".format(x), end="")
        else:
            print("{} ".format(x), end="")
