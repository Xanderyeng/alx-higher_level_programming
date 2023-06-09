#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    argv = sys.argv
    if (len(argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    inputt = int(argv[1])
    oper = int(argv[3])
    if (argv[2] == "+"):
        print("{} + {} = {}".format(inputt, oper, add(inputt, oper)))
    elif (argv[2] == "-"):
        print("{} - {} = {}".format(inputt, oper, sub(inputt, oper)))
    elif (argv[2] == "*"):
        print("{} * {} = {}".format(inputt, oper, mul(inputt, oper)))
    elif (argv[2] == "/"):
        print("{} / {} = {}".format(inputt, oper, div(inputt, oper)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
