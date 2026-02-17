import sys

words = []
n = int(sys.stdin.readline())
for _ in range(n):
    w = sys.stdin.readline().strip()
    if w not in words:
        words.append(w)
words = sorted(words, key = lambda x: (len(x), x))
while len(words) > 0:
    print(words.pop(0))