n, m = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(n)]
arr2 = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    a = []
    for j in range(m):
        a.append(arr1[i][j]+arr2[i][j])
    print(*a)