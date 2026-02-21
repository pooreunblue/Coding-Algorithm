import sys

N, M = map(int, sys.stdin.readline().split())
nhs = {}
for _ in range(N):
    p = sys.stdin.readline().strip()
    nhs[p] = nhs.get(p, 0) + 1
for _ in range(M):
    p = sys.stdin.readline().strip()
    nhs[p] = nhs.get(p, 0) + 1
a = sorted([k for k, v in nhs.items() if v == 2])
print(len(a))
for i in a:
  print(i)