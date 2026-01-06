def solution(polynomial):
    coef = 0
    const = 0
    
    for v in polynomial.split(' + '):
        if v.isdigit():
            const += int(v)
        else:
            coef = coef + 1 if v == 'x' else coef + int(v[:-1])
    
    if coef == 0:
        return str(const)
    elif coef == 1:
        return 'x + ' + str(const) if const != 0 else 'x'
    else:
        return str(coef) + 'x' + ' + ' + str(const) if const != 0 else str(coef) + 'x'