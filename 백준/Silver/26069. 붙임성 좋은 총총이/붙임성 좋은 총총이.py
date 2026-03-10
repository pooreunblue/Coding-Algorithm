import sys

N = int(sys.stdin.readline())
dance = set()
for _ in range(N):
    a, b = sys.stdin.readline().split()
    if a == 'ChongChong' or b == 'ChongChong' or a in dance or b in dance:
        dance.update([a,b])
print(len(list(dance)))