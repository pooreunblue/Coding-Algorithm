import sys

N, M = map(int, sys.stdin.readline().split())
s = set()
cnt = 0
for _ in range(N):
    s.add(sys.stdin.readline())
for _ in range(M):
    message = sys.stdin.readline()
    if message in s:
        cnt += 1
print(cnt)