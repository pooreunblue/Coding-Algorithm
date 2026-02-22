import sys

A, B = map(int, sys.stdin.readline().split())
m = A*B
while B:
    A, B = B, A%B
print(m//A)