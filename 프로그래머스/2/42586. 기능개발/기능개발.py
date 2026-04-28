import math
from collections import deque

def solution(progresses, speeds):
    a = []
    days = deque()
    for i in range(len(progresses)):
        days.append(math.ceil((100-progresses[i])/speeds[i]))
    first = days.popleft()
    cnt = 1
    while days:
        if days[0] <= first:
            cnt += 1
            days.popleft()
        else:
            a.append(cnt)
            first = days[0]
            cnt = 0
    a.append(cnt)
    return a