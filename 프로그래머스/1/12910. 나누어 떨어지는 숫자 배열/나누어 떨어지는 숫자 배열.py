def solution(arr, divisor):
    r = []
    for i in arr:
        if i % divisor == 0:
            r.append(i)
    return [-1] if not r else sorted(r) 