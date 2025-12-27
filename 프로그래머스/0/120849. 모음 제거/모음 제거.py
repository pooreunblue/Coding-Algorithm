def solution(my_string):
    vowels = ['a','i','o','e','u']
    for i in my_string:
        for j in vowels:
            if i == j:
                my_string = my_string.replace(i,'')
    return my_string
