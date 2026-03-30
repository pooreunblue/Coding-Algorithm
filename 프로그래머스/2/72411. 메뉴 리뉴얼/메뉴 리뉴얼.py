from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        menus = []
        for order in orders:
            comb = combinations(sorted(order),c)
            menus += comb

        counts = Counter(menus)
        if len(counts) and max(counts.values()) != 1:
            for menu, count in counts.items():
                if count == max(counts.values()):
                    answer.append(''.join(menu))

    return sorted(answer)