def find(parents, x):
    if parents[x] == x:
        return x
    parents[x] = find(parents, parents[x])
    return parents[x]
def union(x,y,parents,rank):
    xroot = find(parents, x)
    yroot = find(parents, y)
    if xroot != yroot:
        if rank[xroot] > rank[yroot]:
            parents[yroot] = xroot
        elif rank[xroot] < rank[yroot]:
            parents[xroot] = yroot
        else:
            parents[yroot] = xroot
            rank[xroot] += 1
def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    parents = list(range(n))
    rank = [0] * n
    min_cost = 0
    edges = 0
    for edge in costs:
        if edges == n-1:
            break
        x = find(parents, edge[0])
        y = find(parents, edge[1])
        if x != y:
            union(x,y,parents,rank)
            min_cost += edge[2]
            edges += 1
    return min_cost