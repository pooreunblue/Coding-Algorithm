def solution(prices):
    stk = [0]
    a = [0] * len(prices)
    for i in range(1, len(prices)):
        while stk and prices[i] < prices[stk[-1]]:
            j = stk.pop()
            a[j] = i - j
        stk.append(i)
    while stk:
        j = stk.pop()
        a[j] = len(prices) - 1 - j
    return a