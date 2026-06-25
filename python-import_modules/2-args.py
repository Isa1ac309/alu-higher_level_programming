#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    number = len(argv) - 1
    if number == 0:
        print("{} arguments.".format(number))
    elif number == 1:
        print("{} argument:".format(number))
    else:
        print("{} arguments:".format(number))
    for i in range(1, number + 1):
        print("{}: {}".format(i, argv[i]))
