import heapq
from collections import defaultdict

INF = 9999999999

def solution(N, road, K):
    count = 0
    graph = defaultdict(list)
    for from_village, to_village, weight in road:
        graph[from_village].append((to_village, weight))
        graph[to_village].append((from_village, weight))
    distances = [INF] * (N + 1)
    visited = [False] * (N + 1)
    distances[1] = 0
    
    priority_queue = [(0, 1)]
    while priority_queue:
        current_distance, current_village = heapq.heappop(priority_queue)
        if visited[current_village]:
            continue
        visited[current_village] = True
        for neighbor, weight in graph[current_village]:
            new_distance = distances[current_village] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))
    for d in distances:
        if d <= K:
            count += 1
    return count