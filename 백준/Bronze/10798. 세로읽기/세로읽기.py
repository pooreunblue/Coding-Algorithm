s = [list(input()) for _ in range(5)]
a = []
for j in range(15):
    for i in range(5):
        if len(s[i]) <= j:
            continue
        a.append(s[i][j])
print(*a, sep='')