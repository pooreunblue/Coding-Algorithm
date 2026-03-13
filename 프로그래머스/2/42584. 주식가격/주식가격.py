def solution(prices):
    stk = [0]
    n = len(prices)
    a = [0]*n
    for i in range(1, n):
        while stk and prices[i] < prices[stk[-1]]:
            j = stk.pop()
            a[j] = i - j
        stk.append(i)
    while stk:
        j = stk.pop()
        a[j] = n - 1 - j
    return a