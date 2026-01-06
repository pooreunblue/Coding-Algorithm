def solution(numbers):
    numbers = sorted(numbers)
    negative = sum(1 for n in numbers if n < 0)
    if negative < 1:
        return numbers[-2] * numbers[-1]
    else:
        if numbers[0] * numbers[1] < numbers[-2] * numbers[-1]:
            return numbers[-2] * numbers[-1]
        else: return numbers[0] * numbers[1]