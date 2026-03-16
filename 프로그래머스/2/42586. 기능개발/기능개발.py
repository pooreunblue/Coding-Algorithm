import math
def solution(progresses, speeds):
    a = []
    days = [math.ceil((100-p)/s) for p, s in zip(progresses, speeds)]
    distribution_day = days[0]
    cnt = 0
    print(days)
    for i in range(len(progresses)):
        print(distribution_day)
        if days[i] <= distribution_day:
            cnt += 1
        else:
            a.append(cnt)
            distribution_day = days[i]
            cnt = 1
    a.append(cnt)
    return a