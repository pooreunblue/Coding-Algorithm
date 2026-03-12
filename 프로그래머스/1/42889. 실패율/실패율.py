def solution(N, stages):
    unclear = [0] * (N+2)
    for stage in stages:
        unclear[stage] += 1
    fails = { }
    reached = len(stages)
    for i in range(1, N+1):
        if unclear[i] == 0:
            fails[i] = 0
        else:
            fails[i] = unclear[i] / reached
            reached -= unclear[i]
    result = sorted(fails, key=lambda x : fails[x], reverse = True)
    return result