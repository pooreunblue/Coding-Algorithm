def solution(my_string):
    ans = 0
    number = ''
    for i in my_string:
        if i.isdigit():
            number += i
        else:
            if len(number) >= 1:
                ans += int(number)
                number = ''
    if len(number) >= 1:
        ans += int(number)
    return ans
            