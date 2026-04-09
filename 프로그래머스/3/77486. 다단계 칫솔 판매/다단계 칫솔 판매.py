def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    recommend = dict(zip(enroll, referral))
    answer = {member: 0 for member in enroll}
    for i, s in enumerate(seller):
        profits = amount[i] * 100
        while profits > 0 and s != '-':
            answer[s] += profits - profits // 10
            profits //= 10
            s = recommend[s]
    return [answer[member] for member in enroll]