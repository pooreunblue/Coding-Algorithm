numbers = list(map(int, input().split()))
sum_1 = 0
sum_2 = 0
for i in range(len(numbers)):
    if i % 2:
        sum_1 += numbers[i]
    if i % 3 == 2:
        sum_2 += numbers[i]
print(sum_1, round((sum_2/int(len(numbers)/3)),1))