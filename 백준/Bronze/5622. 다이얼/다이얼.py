w = input()
a = 0
for i in w:
    if i in 'ABC':
        a += 2
    elif i in 'DEF':
        a += 3
    elif i in 'GHI':
        a += 4
    elif i in 'JKL':
        a += 5
    elif i in 'MNO':
        a += 6
    elif i in 'PQRS':
        a += 7
    elif i in 'TUV':
        a += 8
    else:
        a += 9
a += len(w)
print(a)