#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    i = 1
    if (len(argv) == 1):
        print("0 arguments.")
    elif (len(argv) == 2):
        print("{} argument:".format(len(argv) - 1))
        print("{}: {}".format(i, argv[i]))
    else:
        print("{} arguments:".format(len(argv) - 1))
        while (i < len(argv)):
            print("{}: {}".format(i, argv[i]))
            i += 1
