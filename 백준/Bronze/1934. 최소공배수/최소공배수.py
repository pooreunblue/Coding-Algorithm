import sys
import math

T = int(sys.stdin.readline())
a = []
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    d = math.gcd(A, B)
    a.append(A*B//d)
print(*a, sep='\n')