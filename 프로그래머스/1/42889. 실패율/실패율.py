def solution(N, stages):
    fail = []
    r = []
    for i in range(1,N+1):
        if i not in stages:
            fail.append(0)
        else:
            fail.append(stages.count(i)/len(stages))
        stages = [j for j in stages if j != i]
    n = len(fail)
    while len(r) < N:
        max_fail = max(fail)
        for i, x in enumerate(fail):
            if x == max_fail:
                r.append(i+1)
                fail[i] = -1
    return r

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