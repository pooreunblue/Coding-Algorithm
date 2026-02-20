import sys

N = int(sys.stdin.readline())
cards = {}
data = list(map(int, sys.stdin.readline().split()))
for i in data:
    if i not in cards:
        cards[i] = 1
    else:
        cards[i] += 1
M = int(sys.stdin.readline())
finds = list(map(int, sys.stdin.readline().split()))
for i in finds:
    if i not in cards:
        cards[i] = 0
    print(cards.get(i), end = ' ')