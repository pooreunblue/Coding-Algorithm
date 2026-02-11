from itertools import combinations

n, m = map(int, input().split())
nums = list(map(int, input().split()))
sums = []
for i in combinations(nums, 3):
    sums.append(sum(i))
result = max([s for s in sums if s <= m], default=None)
print(result)