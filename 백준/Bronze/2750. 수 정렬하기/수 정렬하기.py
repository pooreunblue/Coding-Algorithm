n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))
l = sorted(l, reverse = 1)
for _ in range(n):
    a = l.pop()
    print(a)