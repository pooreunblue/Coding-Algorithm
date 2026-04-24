def solution(s):
    stk = []
    for c in s:
        if not stk or stk[-1] != c:
            stk.append(c)
        elif stk[-1] == c:
            stk.pop()
    return 1 if not stk else 0