def solution(id_pw, db):
    is_valid = True
    for d in db:
        if id_pw[0] == d[0]:
            if id_pw[1] == d[1]:
                return 'login'
            return 'wrong pw'
        else: is_valid = False
    if is_valid == False:
        return 'fail'
        