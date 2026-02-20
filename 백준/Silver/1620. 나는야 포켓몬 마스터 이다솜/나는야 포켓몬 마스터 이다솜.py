import sys

N, M = map(int, sys.stdin.readline().split())
pokedex = {}
q = []
for i in range(1, N+1):
    name = sys.stdin.readline().rstrip()
    pokedex[str(i)] = name
    pokedex[name] = str(i)
for _ in range(M):
    q.append(sys.stdin.readline().rstrip())
for i in q:
    print(pokedex.get(i))