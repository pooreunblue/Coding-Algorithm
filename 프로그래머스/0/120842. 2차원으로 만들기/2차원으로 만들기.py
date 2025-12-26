def solution(num_list, n):
    row = len(num_list) // n
    num_list.reverse()
    array = [[0] * n for _ in range(row)]
    for j in range(row):
        for k in range(n):
            array[j][k] = num_list.pop()
    return array
            