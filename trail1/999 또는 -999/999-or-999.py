numbers = list(map(int, input().split()))
max_value = numbers[0]
min_value = numbers[0]
for i in range(1,len(numbers)-1):
    if numbers[i] > max_value:
        max_value = numbers[i]
    elif numbers[i] < min_value:
        min_value = numbers[i]
print(max_value, min_value)