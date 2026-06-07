N, M = map(int, input().split())
numbers = list(map(int, input().split()))
cnt = 0
for i in range(N):
    if numbers[i] == M:
        cnt += 1
print(cnt)