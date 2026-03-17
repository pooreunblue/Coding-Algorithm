def solution(cards1, cards2, goal):
    n = len(goal)
    while goal:
        if goal[0] in cards1:
            if goal[0] == cards1[0]:
                cards1.pop(0)
                goal.pop(0)
            else:
                return "No"
        elif goal[0] in cards2:
            if goal[0] == cards2[0]:
                cards2.pop(0)
                goal.pop(0)
            else:
                return "No"
        else:
            return "No"
    return "Yes"