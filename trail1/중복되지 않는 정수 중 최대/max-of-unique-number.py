n = int(input())
nums = list(map(int, input().split()))
max_v = 0
is_valid = False
a = [0] * (max(nums)+1)
for n in nums:
    a[n] += 1
for n in nums:
    if a[n] == 1 and n > max_v:
        max_v = n
        is_valid = True
if is_valid == False:
    max_v = -1
print(max_v)