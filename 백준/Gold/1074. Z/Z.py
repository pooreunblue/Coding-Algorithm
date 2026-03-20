import sys

N, r, c = map(int, sys.stdin.readline().split())

def Z(x,y,N):
    cnt = 0
    if N == 1:
        if x == 0 and y == 0:
            pass
        elif x == 0 and y == 1:
            cnt += 1
        elif x == 1 and y == 0:
            cnt += 2
        else: cnt += 3
        return cnt
    else:
        if x < 2**(N-1) and y < 2**(N-1):
            return Z(x, y, N-1)
        elif x < 2**(N-1) and 2**(N-1) <= y < 2**N:
            cnt += 2**(2*N-2)
            return cnt + Z(x,y-2**(N-1), N-1)
        elif 2**(N-1) <= x < 2**N and y < 2**(N-1):
            cnt += 2**(2*N-1)
            return cnt + Z(x-2**(N-1), y, N-1)
        else:
            cnt += (2**(2*N-2))*3
            return cnt + Z(x-2**(N-1), y-2**(N-1), N-1)
        
print(Z(r,c,N))