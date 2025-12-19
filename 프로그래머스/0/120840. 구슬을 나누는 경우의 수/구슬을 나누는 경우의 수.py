def solution(balls, share):
    result = 1
    if share < balls/2:
        for i in range(share):
            result *= (balls-i)
            result /= (share-i)
    else:
        num = balls - share
        for i in range(num):
            result *= (balls-i)
            result /= (num-i)
    return round(result, 4)