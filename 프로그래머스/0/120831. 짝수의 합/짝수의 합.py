def solution(n):
    answer = 0
    for i in range(0, n//2+1):
        answer += i
    return answer*2