def solution(array, n):
    min_diff = 99
    near = 0
    for i in array:
        if min_diff > abs(i-n):
            min_diff = abs(i-n)
            near = i
        elif min_diff == abs(i-n):
            near = min(near, i)
    return near