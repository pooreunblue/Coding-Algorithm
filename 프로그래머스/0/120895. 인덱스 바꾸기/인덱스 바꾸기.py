def solution(my_string, num1, num2):
    char_list = list(my_string)
    c1 = char_list[num1]
    c2 = char_list[num2]
    char_list[num1] = c2
    char_list[num2] = c1
    return ''.join(char_list)