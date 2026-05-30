arr = [0] * 10
num = list(map(int, input().split()))
arr[0] = num[0]
arr[1] = num[1]
for i in range(2, len(arr)):
    arr[i] = (arr[i-2] + arr[i-1]) % 10
for i in range(len(arr)):
    print(arr[i], end=' ')