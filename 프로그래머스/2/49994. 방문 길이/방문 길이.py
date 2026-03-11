def solution(dirs):
    x, y = 0, 0
    path = set()
    moving = {'U':(0,1), 'D':(0,-1), 'R':(1,0), 'L':(-1,0)}
    for dir in dirs:
        nx, ny = x + moving[dir][0], y + moving[dir][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            path.add((x,y,nx,ny))
            path.add((nx,ny,x,y))
            x, y = nx, ny
    return len(path)/2