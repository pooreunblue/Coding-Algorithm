def solution(s):
    cnt = 0
    for _ in range(len(s)):
        stk = []
        is_correct = True
        for c in s:
            if c in ["(", "{", "["]:
                stk.append(c)
            elif c == ")":
                if not stk or stk[-1] != "(":
                    is_correct = False
                    break
                stk.pop()
                is_correct = True
            elif c == "}":
                if not stk or stk[-1] != "{":
                    is_correct = False
                    break
                stk.pop()
                is_correct = True
            elif c == "]":
                if not stk or stk[-1] != "[":
                    is_correct = False
                    break
                stk.pop()
                is_correct = True
        if not stk and is_correct:
            cnt += 1
        s = s[1:] + s[0]
    return cnt