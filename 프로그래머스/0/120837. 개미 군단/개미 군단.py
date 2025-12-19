def solution(hp):
    result = 0
    ap = [5,3,1]
    for i in ap:
        result += hp//i
        hp %= i
    return result