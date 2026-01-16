n, m = map(int, input().split())
a = []
for i in range(1, n+1):
    a.append(str(i))
for _ in range(m):
    t = 0
    i, j = map(int, input().split())
    t = a[i-1]
    a[i-1] = a[j-1]
    a[j-1] = t
print(' '.join(a))