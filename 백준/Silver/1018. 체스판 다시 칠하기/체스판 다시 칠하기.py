n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(input())
min_tile = 32
for i in range(0, n-7):
    for j in range(0, m-7):
        tile = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y) % 2 == 0:
                    if board[x][y] != 'W':
                        tile += 1
                else:
                    if board[x][y] == 'W':
                        tile += 1
        min_tile = min(min_tile, tile, 64-tile)
print(min_tile)