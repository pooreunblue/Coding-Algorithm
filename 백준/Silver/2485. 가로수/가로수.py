import sys
import math

N = int(sys.stdin.readline())
t = []
gap = []
for _ in range(N):
    t.append(int(sys.stdin.readline()))
for i in range(N-1):
    gap.append(t[i+1]-t[i])
print((t[-1]-t[0])//math.gcd(*gap)-(N-2)-1)