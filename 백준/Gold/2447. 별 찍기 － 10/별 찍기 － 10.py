import sys

N = int(sys.stdin.readline())
pattern = [[' '] * N for _ in range(N)]

def star(x,y,N):
    if N == 1:
        pattern[x][y] = '*'
        return
    else:
        M = N // 3
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                else:
                    star(x+i*M, y+j*M, M)
star(0,0,N)
for i in pattern:
    print(''.join(i))