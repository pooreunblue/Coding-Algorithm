N = int(input())
arr = [1]
arr.append(N)
i = 2
while arr[i-1] < 100:
    arr.append(arr[i-2] + arr[i-1])
    i += 1
for n in arr:
    print(n, end=' ')