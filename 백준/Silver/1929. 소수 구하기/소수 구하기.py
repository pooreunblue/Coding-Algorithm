import sys

M, N = map(int, sys.stdin.readline().split())
a = []
for i in range(M, N+1):
    if i == 1:
        continue
    isPrime = True
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        a.append(i)
print(*a, sep='\n')