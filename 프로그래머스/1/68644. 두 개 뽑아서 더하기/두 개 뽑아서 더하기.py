def solution(numbers):
    sums = set([(numbers[i]+numbers[j]) for i in range(len(numbers)) for j in range(i+1, len(numbers))])
    sorted_list = sorted(list(sums))
    return sorted_list