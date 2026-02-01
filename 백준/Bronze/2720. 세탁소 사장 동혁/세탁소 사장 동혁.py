t = int(input())
a = []
for _ in range(t):
    n = int(input())
    n, mod = divmod(n,25)
    a.append(n)
    n, mod = divmod(mod,10)
    a.append(n)
    n, mod = divmod(mod,5)
    a.append(n)
    a.append(mod)
print(*a)