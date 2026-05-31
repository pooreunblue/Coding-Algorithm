n = int(input())
i = 1
cnt = 0
while cnt < 2:
    if not((n*i)%5):
        cnt += 1
    print(n*i, end=' ')
    i += 1