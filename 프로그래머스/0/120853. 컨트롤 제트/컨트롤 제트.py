def solution(s):
    list = s.split()
    remove_list = [(list[i-1]) for i, x in enumerate(list) if x == 'Z']
    for i in remove_list:
        list.remove(i)
    return sum([int(i) for i in list if i not in 'Z'])