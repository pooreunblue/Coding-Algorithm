import sys
import math

N = 123456
is_prime = [True] * (2*N+1)
is_prime[0] = False
is_prime[1] = False

for i in range(2, int(math.sqrt(2*N)) + 1):
    if is_prime[i]:
        for j in range(2 * i, 2*N+1, i):
            is_prime[j] = False
a = []
while True:
  n = int(input())
  cnt = 0
  if n == 0 :
    break
  else:
    cnt = is_prime[n+1:2*n+1].count(True)
    a.append(cnt)
print(*a, sep='\n')