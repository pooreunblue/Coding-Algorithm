from collections import Counter

def solution(participant, completion):
    hash = {}
    for p in participant:
        if p in hash:
            hash[p] += 1
        else:
            hash[p] = 1
    for c in completion:
        hash[c] -= 1
    for k in hash.keys():
        if hash[k] > 0:
            return k