from itertools import combinations

n, m = map(int, input().split())
nums = list(map(int, input().split()))
result = max(sum(n) for n in combinations(nums, 3) if sum(n) <= m)
print(result)