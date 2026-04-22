def solution(msg):
    answer = []
    dict = {chr(i+64): i for i in range(1, 27)}
    i = 0
    while i < len(msg):
        m = msg[i]
        while i + 1 < len(msg) and m + msg[i+1] in dict:
            m += msg[i+1]
            i += 1
        answer.append(dict[m])
        if i + 1 < len(msg):
            dict[m+msg[i+1]] = len(dict) + 1
        i += 1
    return answer