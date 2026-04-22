def solution(msg):
    answer = []
    dict = {str(chr(i+64)): i for i in range(1,27)}
    i = 0
    while i < len(msg):
        w = msg[i]
        while (i + 1 < len(msg)) and (w + msg[i+1] in dict):
            w += msg[i+1]
            i += 1
        answer.append(dict[w])
        if i + 1 < len(msg):
            dict[w + msg[i+1]] = len(dict)+1
        i += 1
    return answer