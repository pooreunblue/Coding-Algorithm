import sys

N, K = map(int, sys.stdin.readline().split())

def factorials(n):
    a = 1
    for i in range(1, n+1):
        a *= i
    return a

print(int(factorials(N)/(factorials(K)*factorials(N-K))))