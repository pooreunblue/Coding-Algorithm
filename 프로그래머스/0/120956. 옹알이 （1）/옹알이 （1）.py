from itertools import permutations

def solution(babbling):
    a = []
    nouns = ['aya', 'ye', 'woo', 'ma']
    for i in range(1, len(nouns)+1):
        for j in permutations(nouns, i):
            a.append(''.join(j))
    return sum(1 for i in babbling if i in a)