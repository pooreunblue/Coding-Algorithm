def solution(order):
    count = 0
    clap_num = ['3','6','9']
    order_num = str(order)
    for i in order_num:
        if i in clap_num:
            count += 1
    return count