import sys


def read_input(string):
    answer = ""
    split_str = string.split(" ")
    for word in split_str:
        if not word.isalpha():
            return "Error"
        else:
            answer += word[0]
    return answer


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Wrong number of arguments")
    else:
        print(read_input(sys.argv[1]))
