import sys


def read_input(count):
    if count > 0:
        line = sys.stdin.readline().strip("\n")
        while count and line:
            if len(line) == 32 and line[0:5] == "00000" and line[5] != '0':
                print(line)
            line = sys.stdin.readline().strip("\n")
            count -= 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Wrong number of arguments")
    else:
        read_input(int(sys.argv[1]))