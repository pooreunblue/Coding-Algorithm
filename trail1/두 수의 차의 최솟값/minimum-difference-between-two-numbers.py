N = int(input())
numbers = list(map(int, input().split()))
min_diff = 99
for i in range(N):
    for j in range(i+1,N):
        diff = numbers[j] - numbers[i]
        if min_diff > diff:
            min_diff = diff
print(min_diff)