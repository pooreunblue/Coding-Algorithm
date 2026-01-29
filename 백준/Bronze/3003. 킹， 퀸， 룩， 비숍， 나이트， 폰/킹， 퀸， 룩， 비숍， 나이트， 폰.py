pieces = list(map(int, input().split()))
sets = [1, 1, 2, 2, 2, 8]
a = []
for i in range(len(sets)):
    a.append(sets[i]-pieces[i])
print(*a)