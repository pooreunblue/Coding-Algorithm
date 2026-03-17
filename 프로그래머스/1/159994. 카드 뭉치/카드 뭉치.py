from collections import deque

def solution(cards1, cards2, goal):
    n = len(goal)
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)
    while goal:
        if cards1 and goal[0] == cards1[0]:
            cards1.popleft()
            goal.popleft()
        elif cards2 and goal[0] == cards2[0]:
            cards2.popleft()
            goal.popleft()
        else:
            break
    return "Yes" if not goal else "No"