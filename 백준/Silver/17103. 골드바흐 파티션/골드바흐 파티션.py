import sys
import math

N = 1000000
prime = [True] * (N+1)
prime[0] = False
prime[1] = False
for i in range(2, int(math.sqrt(N))+1):
    if prime[i]:
        prime[i*i::i] = [False] * len(prime[i*i::i])
primes = [i for i in range(N+1) if prime[i]]

T = int(sys.stdin.readline().strip())
a = []
for _ in range(T):
    cnt = 0
    n = int(sys.stdin.readline().strip())
    for p in primes:
        if p > n // 2:
            break
        if prime[n-p]:
            cnt += 1
    a.append(cnt)
print(*a, sep='\n')