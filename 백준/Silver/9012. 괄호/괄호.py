for _ in range(int(input())):
    stack = []
    answer = 'YES'
    for c in input():
        if c == '(':
            stack.append(c)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                answer = 'NO'
    if len(stack) > 0:
        answer = 'NO'
    
    print(answer)
            