import sys

n = int(sys.stdin.readline())
td = list(map(int, sys.stdin.readline().split()))
print(min(td)*max(td))