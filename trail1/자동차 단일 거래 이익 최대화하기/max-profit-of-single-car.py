n = int(input())
prices = list(map(int, input().split()))
max_profit = 0
for i in range(n):
    for j in range(i+1, n):
        profit = prices[j] - prices[i]
        if profit > max_profit:
            max_profit = profit
print(max_profit)