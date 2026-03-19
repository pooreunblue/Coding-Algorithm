from collections import Counter

def solution(participant, completion):
    uncomplete = Counter(participant) - Counter(completion)
    return list(uncomplete.keys())[0]