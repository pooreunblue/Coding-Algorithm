def solution(keyinput, board):
    xborder = board[0] // 2
    yborder = board[1] // 2
    ans = [0,0]
    for k in keyinput:
        if k == 'up' and ans[1] < yborder:
            ans[1] += 1
        elif k == 'down' and ans[1] > -yborder:
            ans[1] -= 1
        elif k == 'left' and ans[0] > -xborder: 
            ans[0] -= 1
        elif k == 'right' and ans[0] < xborder:
            ans[0] += 1
    return ans