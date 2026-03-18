import sys

def Cantor(N):
    if N == 0:
        return '-'
    else:
        return Cantor(N-1) + ' ' * len(Cantor(N-1)) + Cantor(N-1)

while True:
    try:
        N = int(sys.stdin.readline())
        print(Cantor(N))
    except:
        break