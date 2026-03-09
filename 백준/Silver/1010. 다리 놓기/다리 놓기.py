import sys

T = int(sys.stdin.readline())
a = []
def factorials(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    a.append(int(factorials(M)/(factorials(N)*factorials(M-N))))
print(*a, sep='\n')