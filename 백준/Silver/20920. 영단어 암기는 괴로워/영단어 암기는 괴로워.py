import sys
from collections import Counter

N, M = map(int, sys.stdin.readline().split())
words = [sys.stdin.readline().strip() for _ in range(N)]
vocab = [word for word in words if len(word) >= M]
count = Counter(vocab)
vocab = list(set(vocab))
vocab.sort(key=lambda x: (-count[x], -len(x), x))
print('\n'.join(vocab))