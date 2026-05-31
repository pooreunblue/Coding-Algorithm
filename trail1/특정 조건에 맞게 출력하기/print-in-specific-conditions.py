numbers = list(map(int, input().split()))
arr = []
for number in numbers:
    if number != 0:
        if number % 2 :
            arr.append(number+3)
        elif not (number % 2):
            arr.append(number//2)
    else:
        break
for n in arr:
    print(n, end=' ')