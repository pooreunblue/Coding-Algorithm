sum_odd = 0
sum_even = 0
nums = list(map(int, input().split()))
for i in range(len(nums)):
    if i % 2 == 0:
        sum_odd += nums[i]
    else:
        sum_even += nums[i]
result = sum_odd - sum_even
print(abs(result))