def solution(dots):
    incli = []
    for i in range(len(dots)):
        for j in range(i+1, len(dots)):
            incli.append((dots[j][1]-dots[i][1])/(dots[j][0]-dots[i][0]))
    for i in incli:
        if incli.count(i) % 2 == 0:
            return 1
    return 0