def solution(order):
    count = 0
    clap_num = ['3','6','9']
    for i in clap_num:
        count += str(order).count(i)
    return count