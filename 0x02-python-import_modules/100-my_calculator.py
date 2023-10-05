#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":

    if (len(sys.argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        match sys.argv[2]:
            case "+":
                print("{} + {} = {}".format(a, b, add(a, b)))
            case "-":
                print("{} - {} = {}".format(a, b, sub(a, b)))
            case "*":
                print("{} * {} = {}".format(a, b, mul(a, b)))
            case "/":
                print("{} / {} = {}".format(a, b, div(a, b)))
            case _:
                print("Unknown operator. Available operators: +, -, * and /")
                sys.exit(1)
