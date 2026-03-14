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
        if not basket:
            if stks[m-1]:
                basket.append(stks[m-1].pop())
        else:    
            if stks[m-1]:
                if basket[-1] == stks[m-1][-1]:
                    stks[m-1].pop()
                    basket.pop()
                    cnt += 2
                else:
                    basket.append(stks[m-1].pop())
    return cnt