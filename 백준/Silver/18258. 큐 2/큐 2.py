import sys
from collections import deque

dq = deque()
N = int(sys.stdin.readline())
for _ in range(N):
    c = list(sys.stdin.readline().split())
    if c[0] == 'push':
        dq.append(int(c[1]))
    elif c[0] == 'pop':
        if len(dq) == 0:
            print(-1)
        else: 
            print(dq[0])
            dq.popleft()
    elif c[0] == 'size':
        print(len(dq))
    elif c[0] == 'empty':
        if len(dq) == 0:
            print(1)
        else: print(0)
    elif c[0] == 'front':
        if len(dq) == 0:
            print(-1)
        else: print(dq[0])
    elif c[0] == 'back':
        if len(dq) == 0:
            print(-1)
        else: print(dq[-1])