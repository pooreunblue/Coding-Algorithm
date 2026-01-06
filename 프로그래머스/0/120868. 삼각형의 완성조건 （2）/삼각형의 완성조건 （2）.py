def solution(sides):
    sides.sort()
    if sides[0] != 1:
        return 2 * sides[0] - 1
    return 1