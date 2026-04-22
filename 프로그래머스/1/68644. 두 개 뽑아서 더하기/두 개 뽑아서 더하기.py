def solution(numbers):
    sum = set()
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                sum.add(numbers[i]+numbers[j])
    return sorted(list(sum))