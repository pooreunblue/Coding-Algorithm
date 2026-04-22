def solution(answers):
    result = []
    scores = [0] * 3
    methods = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    for i, method in enumerate(methods):
        for j, answer in enumerate(answers):
            if answer == method[j%len(method)]:
                scores[i] += 1
    max_score = max(scores)
    for i, score in enumerate(scores):
        if score == max_score:
            result.append(i+1)
    return result