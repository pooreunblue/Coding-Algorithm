import sys

subs = set()
S = sys.stdin.readline().strip()
for i in range(len(S)):
  for j in range(len(S)+1):
    subs.add(S[i:j])
print(len(list(subs))-1)