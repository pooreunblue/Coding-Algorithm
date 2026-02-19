import sys

n = int(sys.stdin.readline())
s = set()
for _ in range(n):
    name, state = sys.stdin.readline().split()
    if name not in s and state == 'enter':
        s.add(name)
    elif name in s and state == 'leave':
        s.remove(name)
people = sorted(s, reverse = True)
for p in people:
    print(p)