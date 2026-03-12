def solution(arr):
    n_arr = []
    for i in arr:
        if len(n_arr) == 0 or i != n_arr[-1]:
            n_arr.append(i)
    return n_arr