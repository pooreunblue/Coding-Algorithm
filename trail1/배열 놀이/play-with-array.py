N, Q = map(int, input().split())
numbers = list(map(int, input().split()))
index = 0
for i in range(Q):
    q = list(map(int, input().split()))
    if len(q) == 3:
        for n in range(q[1]-1, q[2]):
            print(numbers[n], end=' ')
        print()
    else:
        if q[0] == 1:
            print(numbers[q[1]-1])
        elif q[0] == 2:
            for j in range(N):
                if numbers[j] == q[1]:
                    index = j+1
                    break
            print(index)
            index = 0
