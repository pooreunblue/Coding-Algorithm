def solution(array):
    answer = 0
    count = 0
    for i in set(array):
        if array.count(i) > count:
            count = array.count(i)
            answer = i
        elif array.count(i) == count:
            answer = -1
    return answer