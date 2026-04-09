def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    recommend = dict(zip(enroll, referral))
    index = {val:i for i, val in enumerate(enroll)}
    for i, s in enumerate(seller):
        profits = amount[i] * 100
        while True:
            tip = profits // 10
            if s == '-':
                break
            if tip == 0:
                answer[index[s]] += profits
                break
            else:
                answer[index[s]] += profits - tip
                profits //= 10
            s = recommend[s]
    return answer