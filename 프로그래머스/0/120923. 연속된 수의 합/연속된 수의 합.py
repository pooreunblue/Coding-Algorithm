def solution(num, total):
    d = 0
    for i in range(num):
        d += i
    a = int((total - d)/num)
    return [i for i in range(a, a+num)]
        