import math

def solution(n):
    list = [math.factorial(i) for i in range(1,11)]
    for i in list:
        if i>n:
            return list.index(i)
        elif i==n:
            return list.index(i)+1
        