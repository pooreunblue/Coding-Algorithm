def solution(board):
    danger = set()
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            if not x:
                continue
            danger.update((i+di, j+dj) for di in [-1, 0, 1] for dj in [-1, 0, 1])
    return len(board)*len(board) - sum(0<=i<len(board) and 0<=j<len(board) for i,j in danger)