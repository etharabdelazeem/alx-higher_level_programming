#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv) - 1
    if (n == 0):
        print("{} arguments.".format(n))
    elif (n == 1):
        print("{} argument:\n{}: {}".format(n, n, argv[n]))
    else:
        print("{} arguments:".format(n))
        for a in range(1, len(argv)):
            print("{}: {}".format(a, argv[a]))
