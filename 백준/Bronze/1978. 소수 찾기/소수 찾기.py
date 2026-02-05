n = int(input())
nums = list(map(int, input().split()))
a = 0
for i in nums:
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        a += 1
print(a)