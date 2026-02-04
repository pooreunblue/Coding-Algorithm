while True:
    n = int(input())
    if n == -1:
        break
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n//i)
    divisors.discard(n)
    a = sorted(divisors)
    s = sum(a)
    if s == n:
        print(f'{n} = ' + ' + '.join(map(str,a)))
    else:
        print(f'{n} is NOT perfect.')