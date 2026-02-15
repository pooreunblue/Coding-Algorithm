import sys

n = int(sys.stdin.readline())
digit = 0
nums = []
while (n // (10 ** digit)) > 0:
    nums.append((n // (10 ** digit)) % 10)
    digit += 1
nums = sorted(nums, reverse=True)
print(''.join(map(str,nums)))