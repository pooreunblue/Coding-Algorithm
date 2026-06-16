n = int(input())
prices = list(map(int, input().split()))
profit = set()
if n == 1:
    print(0)
else:
    for i in range(n):
        for j in range(n):
            if j > i:
                profit.add(prices[j]-prices[i])
    max_profit = max(list(profit))
    if max_profit < 0:
        max_profit = 0
    print(max_profit)