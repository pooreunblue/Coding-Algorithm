def solution(numbers):
    sum = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            sum.add(numbers[i]+numbers[j])
    return sorted(list(sum))