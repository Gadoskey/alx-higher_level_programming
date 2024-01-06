#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arguments = sys.argv[1:]
    if arguments:
        result = sum(map(int, arguments))
        print(result)
    else:
        print(0)
