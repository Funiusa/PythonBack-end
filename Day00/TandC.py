import sys


def read_input():
    tattoo = ""
    count = 0
    for line in sys.stdin.readlines():
        count += 1
        if count > 3 or len(line.strip('\n')) != 5:
            return "Error"
        tattoo += line.strip('\n')
    if tattoo[0] == '*' and tattoo[4:7] == "***" and tattoo[8:11] == "***" \
            and tattoo[12] == '*' and tattoo[-1] == '*':
        if tattoo[1:4] != "***" and tattoo[7] != '*' \
                and tattoo[11] != '*' and tattoo[13] != '*':
            return True
    return False


if __name__ == "__main__":
    print(read_input())
