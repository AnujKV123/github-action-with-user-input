import sys


def add(a, b):
    x = a+b
    return x

a = int(sys.argv[0])
b = int(sys.argv[1])
# c = sys.argv[2]

print(f'sum to {a} and {b} = {add(a, b)}')
# print("Hello ", c)