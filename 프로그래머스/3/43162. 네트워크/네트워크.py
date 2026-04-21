from collections import defaultdict

adj_list = defaultdict(list)
visited = set()

def solution(n, computers):
    count = 0
    for i in range(len(computers)):
        for j in range(len(computers[0])):
            if computers[i][j] == 1:
                if i != j:
                    adj_list[i].append(j)
    for i in range(n):
        if i not in visited:
            count += 1
            dfs(i)
    return count
                    
def dfs(node):
    visited.add(node)
    for adj_node in adj_list.get(node,[]):
        if adj_node not in visited:
            dfs(adj_node)