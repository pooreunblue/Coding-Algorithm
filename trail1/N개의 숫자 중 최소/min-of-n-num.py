N = int(input())
numbers = list(map(int, input().split()))
min_val = numbers[0]
cnt = 0
for n in numbers[1:]:
    if n < min_val:
        min_val = n
for i in range(N):
    if numbers[i] == min_val:
        cnt += 1
print(min_val, cnt)