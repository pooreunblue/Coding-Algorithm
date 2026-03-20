from collections import Counter

def solution(want, number, discount):
    hash = {}
    cnt = 0
    for i in range(len(want)):
        hash[want[i]] = number[i]
    for i in range(len(discount)-9):
        goods = Counter(discount[i:i+10])
        for h in hash.keys():
            if goods[h] != hash[h]:
                break
            else: continue
        else:
            cnt += 1
    return cnt