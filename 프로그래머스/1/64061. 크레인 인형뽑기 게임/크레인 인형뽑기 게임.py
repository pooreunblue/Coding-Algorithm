def solution(board, moves):
    n = len(board)
    cnt = 0
    stks = [[] * n for _ in range(n)]
    basket = []
    for row in reversed(board):
        for i in range(len(row)):
            if row[i]:
                stks[i].append(row[i])
    for m in moves:
        if stks[m-1]:
            doll = stks[m-1].pop()
            if not basket:
                basket.append(doll)
            elif basket[-1] == doll:
                basket.pop()
                cnt += 2
            else:
                basket.append(doll)
    return cnt