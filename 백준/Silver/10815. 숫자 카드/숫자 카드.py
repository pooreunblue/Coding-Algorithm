import sys

n = int(sys.stdin.readline())
s = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
for i in numbers:
    if i in s:
        print(1, end=' ')
    else:
        print(0, end=' ')