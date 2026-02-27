import sys

while True:
    s = sys.stdin.readline().rstrip('\n')
    stk = []
    answer = 'yes'
    if s == '.':
        break
    for c in s:
        if c == '(' or c == '[':
            stk.append(c)
        elif c == ')' :
            if len(stk) == 0 or stk[-1] != '(':
                answer = 'no'
                break
            stk.pop()
        elif c == ']':
            if len(stk) == 0 or stk[-1] != '[':
                answer = 'no'
                break
            stk.pop()
    if len(stk) > 0:
        answer = 'no'
    print(answer)