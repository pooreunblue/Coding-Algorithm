import sys

N = int(sys.stdin.readline().strip())
stk = []
a = []
for _ in range(N):
    c = list(map(int, sys.stdin.readline().split()))
    if len(c) > 1:
        stk.append(c[1])
    if c[0] == 2:
        if any(isinstance(x, int) for x in stk):
            a.append(stk.pop())
        else: a.append(-1)
    elif c[0] == 3:
        a.append(len(stk))
    elif c[0] == 4:
        if len(stk) == 0:
            a.append(1)
        else: a.append(0)
    elif c[0] == 5:
        if any(isinstance(x, int) for x in stk):
            a.append(stk[-1])
        else: a.append(-1)
print(*a, sep='\n')