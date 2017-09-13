import sys

digit_string = sys.argv[1]


def sum_string(string):
    if not string.isdigit():
        print("Не числовая строка")
        return
    lst = [int(c) for c in string]
    return sum(lst)


if __name__ == "__main__":
    print(sum_string(digit_string))