def solution(balls, share):
    if share > balls // 2:
        share = balls - share
        
    result = 1
    for i in range(share):
        result = result * (balls-i) // (i+1)
    return result
    