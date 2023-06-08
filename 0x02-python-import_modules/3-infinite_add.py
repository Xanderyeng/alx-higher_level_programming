#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    i = 1
    infina = 0
    while (i < len(argv)):
        infina = infina + (int(argv[i]))
        i += 1
    print("{}".format(infina))
