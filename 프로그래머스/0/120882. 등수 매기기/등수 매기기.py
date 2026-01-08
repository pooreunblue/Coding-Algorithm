def solution(score):
    scores = sorted([sum(i) for i in score], reverse=True)
    return [scores.index(sum(i))+1 for i in score]