numbers = list(map(int,input().split()))
arr = [0] * 7
for number in numbers:
    arr[number] += 1
for i in range(1,7):
    print(f"{i} - {arr[i]}")