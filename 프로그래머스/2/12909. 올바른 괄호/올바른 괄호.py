def solution(s):
    stk = []
    for c in s:
        if c == "(":
            stk.append(c)
        elif c == ')':
            if stk:
                stk.pop()
            else: 
                return False
    return False if stk else True