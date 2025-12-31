def solution(s):
    ans = []
    for c in s:
        if s.count(c) == 1:
            ans.append(c)
    ans.sort()
    return ''.join(ans)
            