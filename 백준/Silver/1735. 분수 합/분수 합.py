import sys
import math

A, B = map(int, sys.stdin.readline().split())
C, D = map(int, sys.stdin.readline().split())
m = A*D + C*B
d = B*D
print(m//math.gcd(m,d), d//math.gcd(m,d))