import sys

N = int(sys.stdin.readline())
cnt = 0
for _ in range(N):
    t = sys.stdin.readline().strip()
    if t == 'ENTER':
        a = set()
    elif t not in a:
        a.add(t)
        cnt += 1
    elif t in a:
        continue
print(cnt)