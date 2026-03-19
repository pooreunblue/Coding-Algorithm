from collections import Counter

def solution(participant, completion):
    player = Counter(participant)
    complete = Counter(completion)
    player -= complete
    return list(player.keys())[0]