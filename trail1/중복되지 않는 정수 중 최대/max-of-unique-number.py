n = int(input())
nums = list(map(int, input().split()))
max_v = -1
a = [0] * (max(nums)+1)
for n in nums:
    a[n] += 1
for n in nums:
    if a[n] == 1 and n > max_v:
        max_v = n
print(max_v)