n = int(input())
scores = list(map(int, input().split()))
m = max(scores)
print(round(sum(scores)/m*100/n, 2))