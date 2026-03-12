def solution(n, left, right):
    arr = []
    for i in range(left, right+1):
        k = max(i // n, i % n)
        arr.append(k+1)
    return arr

#   0 1 2
# 0 1 2 3
# 1 2 2 3
# 2 3 3 3

# 0 1 2 3 4 5 6 7 8
# 1 2 3 2 2 3 3 3 3

#   0 1 2 3 4 
# 0 1 2 3 4 5
# 1 2 2 3 4 5
# 2 3 3 3 4 5
# 3 4 4 4 4 5
# 4 5 5 5 5 5