import sys
import math

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

def merge_sort(A, p, r):
    if p<r :
        q = math.ceil((p+r)//2)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        return merge(A, p, q, r)
        
def merge(A, p, q, r):
    global cnt, save
    i, j, t = p, q+1, 1
    tmp = []
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
    while i <= q:
        tmp.append(A[i])
        i += 1
    while j <= r:
        tmp.append(A[j])
        j += 1
    i, t = p, 0
    while i <= r:
        A[i] = tmp[t]
        cnt += 1
        if cnt == K:
            save = A[i]
            break;
        i += 1
        t += 1
cnt = 0
save = -1
merge_sort(A, 0, N-1)
print(save)