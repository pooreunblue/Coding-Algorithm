def solution(spell, dic):
    for s in dic:
        if sorted(spell) == sorted(s):
            return 1
    return 2
    