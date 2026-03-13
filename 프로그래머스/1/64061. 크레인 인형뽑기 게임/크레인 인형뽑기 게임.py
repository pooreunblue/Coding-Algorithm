def solution(board, moves):
    n = len(board)
    cnt = 0
    stks = [[] * n for _ in range(n)]
    basket = []
    for i, row in enumerate(reversed(board)):
        for j in range(n):
            if row[j]:
                stks[j].append(row[j])
    for m in moves:
        if stks[m-1]:
            basket.append(stks[m-1].pop())
            if len(basket) >= 2 and basket[-1] == basket[-2]:
                basket.pop()
                basket.pop()
                cnt += 2
    return cnt