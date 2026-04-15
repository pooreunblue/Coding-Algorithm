from collections import deque

def solution(priorities, location):
    order = []
    queue = deque(range(len(priorities)))
    while queue:
        m = max(priorities)
        p = queue.popleft()
        prior = priorities.pop(0)
        if m > prior:
            queue.append(p)
            priorities.append(prior)
        else:
            order.append(p)
    return order.index(location)+1