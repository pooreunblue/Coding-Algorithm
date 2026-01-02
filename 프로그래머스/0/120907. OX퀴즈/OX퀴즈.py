def solution(quiz):
    ans = []
    for f in quiz:
        if eval(f.split(' = ')[0]) == int(f.split(' = ')[1]):
            ans.append('O')
        else: ans.append('X')
    return ans
