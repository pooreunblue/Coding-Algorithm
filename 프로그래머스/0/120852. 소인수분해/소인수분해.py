def solution(n):
    i = 2
    prime_factors = []
    while n >= i:
        if n % i == 0:
            if i not in prime_factors:
                prime_factors.append(i)
            n //= i
        else:
            i += 1
    return prime_factors
        