import sys


def add(a, b):
    x = a+b
    return x

a = int(sys.argv[1])
b = int(sys.argv[2])
# c = sys.argv[3]

print(f'sum to {a} and {b} = {add(a, b)}')
# print("!! Hello", c, "!!")