def solution(A, B):
    a = []
    if B == A:
        return 0
    
    for _ in range(len(A)):
        A = A[-1] + A[:-1]
        a.append(A)
    
    for i in a:
        if B == i:
            return a.index(i)+1
    return -1