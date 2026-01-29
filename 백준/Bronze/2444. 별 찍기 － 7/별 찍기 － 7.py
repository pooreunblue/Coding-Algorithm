n = int(input())
b = n - 1
s = 1
for i in range(n):
    print(' '*b + '*'*s)
    b -= 1
    s += 2
b = 1
s = 2*n - 3
for i in range(n-1):
    print(' '*b + '*'*s)
    s -= 2
    b += 1