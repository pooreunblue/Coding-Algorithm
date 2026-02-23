import sys

N = int(sys.stdin.readline())
a = []
for _ in range(N):
    n = int(sys.stdin.readline())
    if n < 2:
        n = 2
    while n >= 2:
        isPrime = True
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                isPrime = False
                break
        if isPrime:
            break
        else:
            n += 1
    a.append(n)
print(*a, sep='\n')