import sys

data = sys.stdin.read().split()
n = int(data[0])
nums = list(map(int, data[1:]))
nums.sort()
print('\n'.join(map(str, nums)))