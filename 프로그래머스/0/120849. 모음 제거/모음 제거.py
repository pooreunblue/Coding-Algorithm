def solution(my_string):
    vowels = ['a','i','o','e','u']
    for vowel in vowels:
        my_string = my_string.replace(vowel,'')
    return my_string
