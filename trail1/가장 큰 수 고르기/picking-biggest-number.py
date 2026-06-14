numbers = list(map(int, input().split()))
max_val = numbers[0]
for number in numbers[1:]:
    if number > max_val:
        max_val = number
print(max_val)