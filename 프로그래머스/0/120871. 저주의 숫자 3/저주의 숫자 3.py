def solution(n):
    x_list = [i for i in range(1, 201) if '3' not in str(i) and i % 3 != 0]
    return x_list[n-1]