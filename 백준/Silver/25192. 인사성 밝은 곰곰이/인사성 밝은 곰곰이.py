import sys

N = int(sys.stdin.readline())
cnt = 0
a = set()
for _ in range(N):
    t = sys.stdin.readline().strip()
    if t == 'ENTER':
        cnt += len(list(a))
        a = set()
    else:
        a.add(t)
cnt += len(list(a))
print(cnt)