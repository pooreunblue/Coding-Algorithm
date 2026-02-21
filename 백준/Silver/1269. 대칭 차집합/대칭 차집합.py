import sys

A, B = map(int, sys.stdin.readline().split())
aset = set(list(map(int, sys.stdin.readline().split())))
bset = set(list(map(int, sys.stdin.readline().split())))
print(len(list(aset-bset)) + len(bset-aset))