import sys
import math

N = 1000000
prime = [True] * (N+1)
prime[0] = False
prime[1] = False
for i in range(2, int(math.sqrt(N))+1):
    if prime[i]:
        for j in range(2*i, N+1, i):
            prime[j] = False

T = int(sys.stdin.readline().strip())
a = []
for _ in range(T):
    cnt = 0
    n = int(sys.stdin.readline().strip())
    for i in range(2, n//2+1):
        if prime[i] and prime[n-i]:
            cnt += 1
    a.append(cnt)
print(*a, sep='\n')