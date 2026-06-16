numbers = list(map(int, input().split()))
under_max = 0
over_min = 1000
for number in numbers:
    if number < 500 and number > under_max:
        under_max = number
    elif number > 500 and number < over_min:
        over_min = number
print(under_max, over_min)