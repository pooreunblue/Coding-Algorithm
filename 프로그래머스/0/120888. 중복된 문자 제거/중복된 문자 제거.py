def solution(my_string):
    characters = []
    for c in my_string:
        if c not in characters:
            characters.append(c)
    return ''.join(characters)