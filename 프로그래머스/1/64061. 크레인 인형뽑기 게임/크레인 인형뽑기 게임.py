def solution(board, moves):
    cnt = 0
    basket = []
    square = [[] for _ in range(len(board))]
    for i in range(len(board[0])):
        for j in range(len(board)-1, -1, -1):
            square[i].append(board[j][i])
    for move in moves:
        while square[move-1] and square[move-1][-1] == 0:
            square[move-1].pop()
        if square[move-1]:
            basket.append(square[move-1].pop())
        else:
            continue
        if len(basket) >= 2 and basket[-1] == basket[-2]:
            basket.pop()
            basket.pop()
            cnt += 2
    return cnt