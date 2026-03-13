def solution(s):
    stk = []
    for c in s:
        if stk and stk[-1] == c:
            stk.pop()
        else:
            stk.append(c)
    return 1 if not stk else 0