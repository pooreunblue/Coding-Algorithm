def solution(s):
    stk = []
    for c in s:
        if not stk:
            stk.append(c)
        elif stk[-1] == c:
            stk.pop()
        else:
            stk.append(c)
    if not stk:
        return 1
    return 0