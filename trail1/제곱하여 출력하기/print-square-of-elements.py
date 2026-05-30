N = int(input())
numbers = list(map(int, input().split()))
result = [num ** 2 for num in numbers]
for n in result:
    print(n, end=' ')