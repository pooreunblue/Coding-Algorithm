s = "}]()[{"
def solution(s):
    cnt = 0
    for _ in range(len(s)):
        stk = []
        for c in s:
            if c == '[' or c == '(' or c == '{':
                stk.append(c)
            else: 
                if not stk:
                    break
                elif c == ']' and stk[-1] == '[':
                    stk.pop()
                elif c == ')' and stk[-1] == '(':
                    stk.pop()
                elif c == '}' and stk[-1] == '{':
                    stk.pop()
                else:
                    break
        else:
            if not stk:
                cnt += 1
        s = s[1:] + s[0]
    return cnt