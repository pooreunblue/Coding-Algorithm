N = int(input())
numbers = list(map(int, input().split()))
cnt = 0
idx = 0
for i in range(N):
    if numbers[i] == 2:
        cnt += 1
        if cnt == 3:
            idx = i+1
            break
print(idx)