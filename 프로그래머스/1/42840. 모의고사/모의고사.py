def solution(answers):
    a = []
    supo = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    scores = [0] * 3
    for j, numbers in enumerate(supo):
        for i, answer in enumerate(answers):
            if answer == numbers[i % len(numbers)]:
                scores[j] += 1
    max_scores = max(scores)
    for i, score in enumerate(scores):
        if score == max_scores:
            a.append(i+1)
    return sorted(a)