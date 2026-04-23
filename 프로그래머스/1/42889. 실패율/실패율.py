def solution(N, stages):
    unclear = [0] * (N+2) # 도달했지만 클리어하지 못한 플레이어의 수
    for stage in stages:
        unclear[stage] += 1
    fails = { }
    reached = len(stages) # 스테이지에 도달한 플레이어 수
    for i in range(1, N+1): # 1번 스테이지부터 N번 스테이지까지
        if unclear[i] == 0:
            fails[i] = 0
        else:
            fails[i] = unclear[i] / reached
            reached -= unclear[i]
    result = sorted(fails, key=lambda x : fails[x], reverse = True)
    return result