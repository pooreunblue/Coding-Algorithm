def solution(array, n):
    min_diff = 99
    near = 0
    array.sort()
    for i in array:
        if min_diff > abs(i-n):
            min_diff = abs(i-n)
            near = i
    return near