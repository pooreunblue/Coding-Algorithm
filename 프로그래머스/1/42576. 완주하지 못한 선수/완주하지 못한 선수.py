from collections import Counter

def solution(participant, completion):
    player = Counter(participant)
    complete = Counter(completion)
    player -= complete
    uncomplete = list(player.keys())
    return uncomplete[0]