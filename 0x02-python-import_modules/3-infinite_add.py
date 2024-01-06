#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num = len(sys.argv) - 1
    total_addition = 0
    for i in range(num):
        total_addition = total_addition + int(sys.argv[i + 1])
    print("{}".format(total_addition))
