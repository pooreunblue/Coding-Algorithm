import sys
from collections import deque

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
C = list(map(int, sys.stdin.readline().split()))
dq = deque()
a = []

for i in range(N):
    if A[i] == 0:
        dq.append(B[i])
if len(dq) > 0:
    for c in C:
        dq.appendleft(c)
        a.append(dq.pop())
else:
    print(*C)
print(*a)