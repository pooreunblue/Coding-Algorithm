words = input()
dials = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = 0
for w in words:
    for i in range(len(dials)):
        if w in dials[i]:
            a += i+3
print(a)