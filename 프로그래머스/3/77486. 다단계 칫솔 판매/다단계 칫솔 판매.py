def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    recommend = dict(zip(enroll, referral))
    index = {val:i for i, val in enumerate(enroll)}
    for i, s in enumerate(seller):
        profits = amount[i] * 100
        while profits > 0 and s != '-':
            answer[index[s]] += profits - profits // 10
            profits //= 10
            s = recommend[s]
    return answer