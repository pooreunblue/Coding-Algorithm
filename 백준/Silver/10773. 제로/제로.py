import sys

K = int(sys.stdin.readline().strip())
stk = []
for _ in range(K):
    n = int(sys.stdin.readline().strip())
    if n == 0:
        stk.pop()
    else:
        stk.append(n)
print(sum(stk))