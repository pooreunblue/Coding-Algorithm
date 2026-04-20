import sys
from collections import defaultdict, deque

adj_list = defaultdict(list)
visited = set()
N, M, R = map(int, sys.stdin.readline().split())
order = [0] * (N+1)
for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

def bfs(start):
    queue = deque([start])
    visited.add(start)
    order[start] = len(visited)
    while queue:
        node = queue.popleft()
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                order[neighbor] = len(visited)
for node in adj_list:
    adj_list[node].sort()            
bfs(R)
for i in order[1:]:
    print(i)