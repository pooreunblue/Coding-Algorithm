import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 6)

adj_list = defaultdict(list)
visited = set()
N, M, R = map(int, sys.stdin.readline().split())
order = [0] * (N+1)
i = 1
for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

def dfs(node):
    visited.add(node)
    order[node] = len(visited)
    for neighbor in adj_list[node]:
        if neighbor not in visited:
            dfs(neighbor)
            
for node in adj_list:
    adj_list[node].sort(reverse=True)
dfs(R)
for i in order[1:]:
    print(i)