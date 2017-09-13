import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])


def discrinimant(a, b, c):
    return b ** 2 - 4 * a * c


def find_solution():
    d = discrinimant(a, b, c)
    x1 = (-b + d ** 0.5) / 2 * a
    x2 = (-b - d ** 0.5) / 2 * a
    return x1, x2


if __name__ == "__main__":
    [print(int(x)) for x in find_solution()]

