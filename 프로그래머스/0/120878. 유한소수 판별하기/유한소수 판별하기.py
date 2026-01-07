import math

def solution(a, b):
    denom = int(b / math.gcd(a, b))
    while denom % 2 == 0:
        denom //= 2
    while denom % 5 == 0:
        denom //= 5
    if denom == 1 or a % b == 0:
        return 1
    return 2
    