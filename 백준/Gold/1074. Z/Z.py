import sys

N, r, c = map(int, sys.stdin.readline().split())

def Z(x,y,N):
    if N == 1:
        if x == 0 and y == 0:
            return 0
        elif x == 0 and y == 1:
            return 1
        elif x == 1 and y == 0:
            return 2
        else: return 3
    else:
        if x < 2**(N-1) and y < 2**(N-1):
            return Z(x, y, N-1)
        elif x < 2**(N-1) and 2**(N-1) <= y < 2**N:
            return 2**(2*N-2) + Z(x,y-2**(N-1), N-1)
        elif 2**(N-1) <= x < 2**N and y < 2**(N-1):
            return 2**(2*N-1) + Z(x-2**(N-1), y, N-1)
        else: 
            return (2**(2*N-2))*3 + Z(x-2**(N-1), y-2**(N-1), N-1)
        
print(Z(r,c,N))