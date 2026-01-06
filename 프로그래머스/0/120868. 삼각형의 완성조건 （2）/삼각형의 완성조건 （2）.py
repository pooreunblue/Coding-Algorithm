def solution(sides):
    cnt = 0
    sides.sort()
    if sides[0] + sides[1] - sides[1] - 1 != 0:
        cnt = cnt + 2 * sides[0] - 1
    else:
        cnt += 1
    return cnt