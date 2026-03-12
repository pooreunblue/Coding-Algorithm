def solution(arr):
    n_arr = []
    n_arr.append(arr[0])
    for i in arr:
      if i != n_arr[-1]:
        n_arr.append(i)
    return n_arr