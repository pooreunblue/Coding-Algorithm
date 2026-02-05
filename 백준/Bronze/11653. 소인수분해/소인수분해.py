n = int(input())
a = []
i = 2
while n != 1:
    if n % i == 0:
        n //= i
        a.append(i)
    else:
        i += 1
print(*a, sep='\n')