numbers = list(map(int, input().split()))
arr = [0] * 10
for number in numbers:
    if number == 0:
        break
    arr[number//10] += 1
for i in range(1,10):
    print(f"{i} - {arr[i]}")