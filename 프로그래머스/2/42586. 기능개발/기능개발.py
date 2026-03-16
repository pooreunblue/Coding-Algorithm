import math
from collections import deque

def solution(progresses, speeds):
    days = deque()
    a = []
    for i in range(len(progresses)): 
        days.append(math.ceil((100-progresses[i])/speeds[i]))
    progress_1 = days.popleft()
    cnt = 1
    while days:
        p = days.popleft()
        if p <= progress_1:
            cnt += 1
        else:
            a.append(cnt)
            progress_1 = p
            cnt = 1
    a.append(cnt)
    return a