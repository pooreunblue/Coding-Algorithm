from collections import defaultdict

def solution(clothes):
    custom = defaultdict(int)
    result = 1
    for cloth in clothes:
        custom[cloth[1]] += 1
    for c in custom:
        result *= custom[c]+1
    result -= 1
    return result