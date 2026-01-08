def solution(score):
    board = []
    for i in score:
        board.append(i[0] + i[1])
    rank = sorted(board, reverse=True)
    return [rank.index(i)+1 for i in board]