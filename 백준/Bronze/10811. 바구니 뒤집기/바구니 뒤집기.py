n, m = map(int, input().split())
numbers = []
for i in range(1, n+1):
    numbers.append(str(i))
for _ in range(m):
    i, j = map(int, input().split())
    numbers = numbers[:i-1]+ numbers[i-1:j][::-1]+numbers[j:]
print(' '.join(numbers))