arr = []
numbers = list(map(int, input().split()))
arr.append(numbers[0])
arr.append(numbers[1]) 
for i in range(2,10):
    arr.append(2*arr[i-2] + arr[i-1])
for n in arr:
    print(n, end=' ')