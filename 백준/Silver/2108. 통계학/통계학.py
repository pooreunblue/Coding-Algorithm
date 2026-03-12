import sys
from collections import Counter

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]
mean = sum(nums) / len(nums)
mid = sorted(nums)[int(N/2)]
cnts = Counter(nums)
max_freq = max(cnts.values())
modes = sorted([k for k, cnt in cnts.items() if cnt == max_freq])
print(round(mean))
print(mid)
if len(modes)>1:
    print(modes[1])
else:
    print(modes[0])
print(max(nums)-min(nums))