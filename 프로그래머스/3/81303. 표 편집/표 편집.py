def solution(n, k, cmd):
    delete = []
    up = [i-1 for i in range(n+2)]
    down = [i+1 for i in range(n+2)]
    k += 1
    for i in cmd:
        if i == 'C':
            delete.append(k)
            up[down[k]] = up[k]
            down[up[k]] = down[k]
            k = up[k] if down[k] > n else down[k]
        elif i == 'Z':
            restore = delete.pop()
            up[down[restore]] = restore
            down[up[restore]] = restore
        else:
            dir, num = i.split()
            if dir == 'U':
                for _ in range(int(num)):
                    k = up[k]
            else:
                for _ in range(int(num)):
                    k = down[k]
        
    a = ['O']*n
    for i in delete:
        a[i-1] = 'X'
    return(''.join(a))