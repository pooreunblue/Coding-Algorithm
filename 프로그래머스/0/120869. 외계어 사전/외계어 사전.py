def solution(spell, dic):
    ans = 1
    arr = []
    for s in dic:
        for c in spell:
            if s.count(c) != 1:
                s = s.replace(s,'')
        if s != '':
            arr.append(s)
    if len(arr) < 1:
        ans += 1
    return ans
    