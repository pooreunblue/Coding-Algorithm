N = int(input())
numbers = list(map(int, input().split()))
result = []
index = N
while True:
    max_n = max(numbers)
    index = numbers.index(max_n)
    result.append(index+1)
    numbers = numbers[:index]
    if index+1 == 1:
        break
for r in result:
    print(r, end=' ')