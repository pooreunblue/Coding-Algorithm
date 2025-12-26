def solution(n):
    count = 0
    for i in range(4, n+1):
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                count += 1
                break
    return count
        