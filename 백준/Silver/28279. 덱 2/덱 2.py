from collections import deque
import sys

dq = deque()
N = int(sys.stdin.readline())
for _ in range(N):
    c = list(sys.stdin.readline().split())
    if c[0] == '1':
        dq.appendleft(int(c[1]))
    elif c[0] == '2':
        dq.append(int(c[1]))
    elif c[0] == '3':
        if len(dq) > 0:
            print(dq[0])
            dq.popleft()
        else: print(-1)
    elif c[0] == '4':
        if len(dq) > 0:
            print(dq[-1])
            dq.pop()
        else: print(-1)
    elif c[0] == '5':
        print(len(dq))
    elif c[0] == '6':
        if len(dq) == 0:
            print(1)
        else: print(0)
    elif c[0] == '7':
        if len(dq) > 0:
            print(dq[0])
        else: print(-1)
    elif c[0] == '8':
        if len(dq) > 0:
            print(dq[-1])
        else: print(-1)